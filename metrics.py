"""Derived metrics for the Duolingo Max teardown.

Every reported figure is taken from Duolingo's own quarterly shareholder
letters filed with the SEC (sources in README). Nothing here is estimated
except where a function name says so, and the prior-year figures are
back-computed from the stated YoY growth rates, which carries the rounding
error of those published percentages.

  python3 metrics.py
"""

# --- As reported, Q1 and Q2 FY2026 shareholder letters ----------------------
Q = {
    "Q1 FY26": {
        "date": "2026-03-31",
        "dau_m": 56.5, "dau_yoy": 0.21,
        "mau_m": 137.8, "mau_yoy": 0.058,
        "paid_m": 12.5, "paid_yoy": 0.21,
        "revenue_m": 292.0, "revenue_yoy": 0.27,
        "bookings_m": 308.5, "bookings_yoy": 0.14,
        "subscription_revenue_m": 250.9,
    },
    "Q2 FY26": {
        "date": "2026-06-30",
        "dau_m": 58.7, "dau_yoy": 0.23,
        "mau_m": 140.6, "mau_yoy": 0.10,
        "paid_m": 12.7, "paid_yoy": 0.17,
        "revenue_m": 298.5, "revenue_yoy": 0.18,
        "bookings_m": 289.1, "bookings_yoy": 0.08,
        "subscription_revenue_m": 258.0,
    },
}
# List prices, US, as advertised in 2026. Secondary sources, and they vary by
# region and promotion - treat as approximate.
PRICES = {
    "Super": {"monthly": 16.99, "annual": 119.99},
    "Max": {"monthly": 29.99, "annual": 167.99},
}
# ---------------------------------------------------------------------------


def prior_year(value, yoy):
    """Back-compute the year-ago figure from a published growth rate.
    Inherits the rounding error of the published percentage."""
    return value / (1 + yoy)


def derive(q):
    d = dict(q)
    d["dau_mau_pct"] = 100 * q["dau_m"] / q["mau_m"]
    d["paid_per_mau_pct"] = 100 * q["paid_m"] / q["mau_m"]
    d["paid_per_dau_pct"] = 100 * q["paid_m"] / q["dau_m"]
    d["sub_rev_share_pct"] = 100 * q["subscription_revenue_m"] / q["revenue_m"]
    # Quarterly subscription revenue per paid subscriber, then monthly.
    d["arpps_quarter"] = q["subscription_revenue_m"] / q["paid_m"]
    d["arpps_month"] = d["arpps_quarter"] / 3
    d["bookings_minus_revenue_m"] = q["bookings_m"] - q["revenue_m"]
    d["bookings_over_revenue"] = q["bookings_m"] / q["revenue_m"]
    return d


if __name__ == "__main__":
    rows = {k: derive(v) for k, v in Q.items()}

    print("AS REPORTED")
    for name, d in rows.items():
        print(f"\n{name} ({d['date']})")
        print(f"  DAU        {d['dau_m']:>6.1f}M   {d['dau_yoy']:+.0%}")
        print(f"  MAU        {d['mau_m']:>6.1f}M   {d['mau_yoy']:+.1%}")
        print(f"  Paid subs  {d['paid_m']:>6.1f}M   {d['paid_yoy']:+.0%}")
        print(f"  Revenue   ${d['revenue_m']:>6.1f}M   {d['revenue_yoy']:+.0%}")
        print(f"  Bookings  ${d['bookings_m']:>6.1f}M   {d['bookings_yoy']:+.0%}")

    print("\n\nDERIVED")
    hdr = f"{'':<28}" + "".join(f"{k:>12}" for k in rows)
    print(hdr)
    for label, key, fmt in [
        ("DAU / MAU", "dau_mau_pct", "{:.1f}%"),
        ("paid / MAU", "paid_per_mau_pct", "{:.2f}%"),
        ("paid / DAU", "paid_per_dau_pct", "{:.1f}%"),
        ("subscription rev share", "sub_rev_share_pct", "{:.1f}%"),
        ("sub rev / paid sub / mo", "arpps_month", "${:.2f}"),
        ("bookings - revenue", "bookings_minus_revenue_m", "${:+.1f}M"),
        ("bookings / revenue", "bookings_over_revenue", "{:.3f}"),
    ]:
        print(f"{label:<28}" + "".join(
            f"{fmt.format(rows[k][key]):>12}" for k in rows))

    print("\n\nTHE DIVERGENCE")
    q1, q2 = rows["Q1 FY26"], rows["Q2 FY26"]
    print(f"  engagement  DAU YoY   {q1['dau_yoy']:+.0%} -> {q2['dau_yoy']:+.0%}"
          f"   ACCELERATING")
    print(f"              MAU YoY   {q1['mau_yoy']:+.1%} -> {q2['mau_yoy']:+.0%}"
          f"   ACCELERATING")
    print(f"  monetization paid YoY {q1['paid_yoy']:+.0%} -> {q2['paid_yoy']:+.0%}"
          f"   decelerating")
    print(f"              rev YoY   {q1['revenue_yoy']:+.0%} -> {q2['revenue_yoy']:+.0%}"
          f"   decelerating")
    print(f"              bkgs YoY  {q1['bookings_yoy']:+.0%} -> {q2['bookings_yoy']:+.0%}"
          f"   decelerating hard")

    print("\n  Bookings vs revenue crossover:")
    for name, d in rows.items():
        rel = "ABOVE" if d["bookings_minus_revenue_m"] > 0 else "BELOW"
        print(f"    {name}: bookings ${d['bookings_m']:.1f}M is {rel} "
              f"revenue ${d['revenue_m']:.1f}M "
              f"({d['bookings_minus_revenue_m']:+.1f}M)")
    print("    Bookings lead revenue for a subscription business, so bookings")
    print("    falling below recognised revenue is the earlier signal.")

    print("\n\nWHERE THE BLENDED ARPU SITS vs LIST PRICES")
    blended = rows["Q2 FY26"]["arpps_month"]
    print(f"  blended subscription revenue per paid sub  ${blended:.2f}/mo")
    for tier, p in PRICES.items():
        print(f"  {tier:<6} list: ${p['monthly']:.2f}/mo, "
              f"${p['annual']:.2f}/yr = ${p['annual']/12:.2f}/mo annualized")
    print(f"\n  The blend sits BELOW even Super's annualized price "
          f"(${PRICES['Super']['annual']/12:.2f}).")
    print("  So the blend is dominated by annual, family and regional pricing,")
    print("  and it does NOT cleanly isolate Max's share. It bounds the size of")
    print("  any large high-ARPU cohort, but it is not proof about Max alone.")

    print("\n  Back-computed year-ago bookings (from published YoY):")
    for name, d in rows.items():
        py = prior_year(d["bookings_m"], d["bookings_yoy"])
        pyr = prior_year(d["revenue_m"], d["revenue_yoy"])
        print(f"    {name[:2]} FY25: bookings ~${py:.1f}M vs revenue ~${pyr:.1f}M "
              f"({py - pyr:+.1f}M)")
