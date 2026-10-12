# Teardown: Duolingo is dismantling its own AI premium tier

A teardown of Duolingo Max built from the company's own SEC filings rather
than press coverage.

**The argument:** Duolingo launched Max as an AI upsell and is now steadily
moving its AI features *down* the price ladder, into cheaper tiers and the free
app. The quarterly numbers point at why. Engagement is speeding up while
monetization slows down, and the company has picked engagement.

Every figure here comes from a quarterly shareholder letter. The derivation is
in [`metrics.py`](metrics.py), so `python3 metrics.py` reproduces all of it.

---

## 1. What Max was sold as

Max launched at the top of a three-tier ladder (Free, Super, Max) and
justified its price with three AI features:

| Feature | What it does |
|---|---|
| **Explain My Answer** | Plain-language explanation of why your answer was right or wrong |
| **Roleplay** | Scripted real-world scenarios with AI feedback on accuracy and vocabulary |
| **Video Call** | Live conversation with Lily, an AI character |

Max lists at **$29.99/month or $167.99/year**, against Super at **$16.99/month
or $119.99/year** (US list prices; both vary by region and promotion). Max is
available in a subset of courses (Spanish, French, German, Italian,
Portuguese, Japanese, Korean, Chinese), not the full catalogue.

## 2. Both of the original differentiators have been de-premiumized

Coverage of Max mostly missed this, probably because it happened quietly across
two quarters of filings instead of in a launch announcement.

| Feature | Launched as | Status now |
|---|---|---|
| Explain My Answer | Max-exclusive | **Free for all users** since 1 Jan 2026 |
| Video Call | Max-exclusive | **Moving into Super.** "Most new Super Duolingo subscribers now have access to Video Call, and we expect to extend that access to existing Super subscribers later this year" (Q2 FY26 letter) |
| Roleplay | Max-exclusive | Still Max |

The Video Call migration is visible as a deliberate sequence, not a one-off.
Q1 FY26 says they are *"starting to expand access to Video Call to Super
subscribers."* Q2 FY26 says *most new* Super subscribers have it and existing
ones are next. That is a planned rollout down a tier, executed over at least
two quarters.

Max launched with three AI differentiators and has one left. A tier whose
exclusives keep moving downward isn't a tier anyone is defending.

## 3. The numbers that explain it

```
                              Q1 FY26     Q2 FY26
DAU                             56.5M       58.7M        +21% -> +23%   accelerating
MAU                            137.8M      140.6M       +5.8% -> +10%   accelerating
Paid subscribers                12.5M       12.7M         +21% -> +17%  decelerating
Revenue                       $292.0M     $298.5M         +27% -> +18%  decelerating
Bookings                      $308.5M     $289.1M         +14% ->  +8%  decelerating hard
```

Two readings matter.

**Engagement and monetization are going opposite ways.** DAU growth went up.
Revenue growth fell nine points and bookings growth fell six. DAU/MAU improved
to 41.7%, so people are using it more, while paid-per-DAU actually *fell* from
22.1% to 21.6%. Duolingo is winning usage faster than it's converting it.

**Bookings crossed below revenue, which is the earlier signal.** In a
subscription business bookings lead recognised revenue, so the gap between them
tells you something about the next few quarters:

```
Q1 FY25:  bookings ~$270.6M vs revenue ~$229.9M   +$40.7M
Q2 FY25:  bookings ~$267.7M vs revenue ~$253.0M   +$14.7M
Q1 FY26:  bookings  $308.5M vs revenue  $292.0M   +$16.5M
Q2 FY26:  bookings  $289.1M vs revenue  $298.5M    -$9.4M   <- crossover
```

Q2 against Q2 is like-for-like, so seasonality doesn't explain the swing from
+$14.7M to -$9.4M. (The FY25 figures are back-computed from published YoY rates
and carry that rounding error.) Revenue growth of 18% is partly just
recognition of bookings already made. The 8% is what the next few quarters get
built from.

**The blended ARPU doesn't leave much room for a big Max cohort.** Subscription
revenue per paid subscriber, blended across everyone, is **$6.77/month**:

```
blended, all paid subscribers        $6.77 / mo
Super, annualized ($119.99/yr)      $10.00 / mo
Max,   annualized ($167.99/yr)      $14.00 / mo
```

The blend sits below even Super's annualized price, which says the base is
mostly annual, family and regionally-priced plans. That's a bound rather than a
proof. It limits how big any high-ARPU group can be, but it doesn't isolate
Max's share, and I shouldn't claim more than that. Duolingo doesn't disclose
Max subscribers, revenue or churn at all.

## 4. Why I think they are doing it

Three hypotheses, in the order I find them convincing:

**1. Max was mispriced against its own cost curve, and inference got cheap.**
Max was priced when live AI conversation was expensive to serve. If per-minute
inference cost has fallen enough, the margin case for gating Video Call behind
$29.99 weakens, and the engagement case for putting it in Super, where it can
touch millions rather than a sliver, gets strong. The company says as much
obliquely: it is looking for *"ways to monetize that are not at odds with user
growth."* That sentence is only necessary if you have concluded your current
monetization *is* at odds with user growth.

**2. Max's conversion wasn't the problem. Its reach was.** At $29.99, Max is
priced for a learner with a deadline: an exam, a move, a job. Most of
Duolingo's 58.7M DAU are casual streak-keepers for whom no AI feature justifies
tripling their bill. Moving features into Super converts a narrow high-ARPU
product into a broad retention lever, which is the right trade when DAU/MAU is
your engine.

**3. Free AI features are a retention and moat play, not a monetization one.**
Explain My Answer going free costs Duolingo the upsell but makes the free tier
materially better at the exact moment competitors can ship a language tutor as
a thin wrapper over a frontier model. A great free tier is a harder thing to
clone than a premium tier.

I am least sure about (1), because it rests on a cost curve I cannot see.

## 5. What I would do differently

**I would not have launched Max as a tier.** The three features had different
natural homes and were bundled by price point rather than by job:

- **Explain My Answer** is a *correctness* feature. It belongs in the core loop
  for everyone, which is where it ended up two years later. Gating the
  explanation of a mistake behind the top tier taxes exactly the moment of
  learning.
- **Video Call** is an *engagement* feature. It belongs wherever it maximises
  habit formation, which is Super, and that's what's happening now.
- **Roleplay** is the only one with a genuine high-intent, high-willingness-to-pay
  job behind it: rehearsing a specific real situation before you are in it.
  That is the deadline-driven learner, and it is the one feature still in Max.

The sequence of de-premiumization reads like a company discovering this
ordering empirically and expensively, one tier migration at a time.

**The better structure is probably not a tier at all.** Roleplay's value scales
with usage intensity before a specific event, which argues for a consumable
(scenario packs, or an exam-prep window) rather than a monthly subscription a
casual learner will never buy and an intense learner only needs for six weeks.

## 6. What I would watch, and what would change my mind

| Signal | What it would tell me |
|---|---|
| Bookings growth re-accelerating above revenue growth | The de-premiumization is working; new volume is replacing lost ARPU. My read is wrong. |
| Max getting a *new* exclusive feature | Duolingo still believes in the tier and I have mistaken sequencing for retreat. |
| Roleplay moving into Super too | Max is being wound down in all but name. |
| Paid-per-DAU resuming growth | Engagement is converting again and the split in section 3 was transitional. |
| A consumable or exam-prep SKU appearing | Lines up with section 5. The job, not the tier, is becoming the unit of sale. |
| Max disappearing from the signup flow | There is **unconfirmed** secondary reporting that Max has stopped appearing as a new-subscription option on some accounts in late 2026. If a filing or Duolingo's own pricing page confirms it, the thesis moves from "not the vehicle they are betting on" to "being retired." I could not verify this in any primary source and do not rely on it above. |

The honest counter-argument to this whole teardown: **a company with 23% DAU
growth and 86% subscription revenue is not in trouble**, and deliberately
trading near-term ARPU for audience at this stage of a category can be exactly
right. My claim is narrower than "this is going badly." It is that *Max, as a
tier, isn't the vehicle they're betting on*, and that the evidence for it sits
in the migrations rather than the growth rates.

## 7. Limitations

- **Duolingo does not disclose Max subscribers, Max revenue, or Max churn.**
  Everything in section 3 about Max's size is inferred from blended ARPU. A
  single disclosed Max number could overturn it.
- FY25 comparatives are back-computed from published YoY percentages and
  inherit their rounding.
- Two quarters is a short series. The bookings crossover is one data point in
  one quarter, and one quarter is a fact, not a trend.
- I have no access to Duolingo's cost per Video Call minute, which hypothesis
  (1) in section 4 depends on entirely.
- Feature-availability details for Explain My Answer come from secondary
  coverage, not a Duolingo filing or blog post; the Video Call tier migration
  is quoted directly from the filings.

## Sources

Primary sources, Duolingo shareholder letters filed with the SEC:
- [Q2 FY2026 shareholder letter (period ended 2026-06-30)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm)
- [Q1 FY2026 shareholder letter (period ended 2026-03-31)](https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/q1fy26duolingo3-31x26share.htm)
- [Form 10-Q, period ended 2026-06-30](https://www.sec.gov/Archives/edgar/data/0001562088/000162828026053603/duol-20260630.htm)
- [Form 10-Q, period ended 2026-03-31](https://www.sec.gov/Archives/edgar/data/0001562088/000162828026029976/duol-20260331.htm)

Secondary sources, for feature availability and pricing:
- [Duolingo makes Explain My Answer free for all users in 2026](https://gamesbeat.com/duolingo-makes-its-ai-powered-explain-my-answer-feature-free-for-all-users-in-2026/) (GamesBeat)
- [Duolingo's 2026 Strategy: The Road to 100 Million DAUs](https://www.classcentral.com/report/duolingo-2026-strategy/) (Class Central)
- [Duolingo Max Explained: $168/Year AI Conversations](https://beginnersinai.org/duolingo-max-explained/) (Beginners in AI)
- [How Much Does Duolingo Cost in 2026](https://languageappguide.com/pricing/duolingo-cost/) (Language App Guide), for Super and Max list prices
- [Super Duolingo](https://www.duolingo.com/super) and [What is Duolingo Max?](https://www.duolingo.com/help/what-is-duolingo-max), Duolingo's own tier pages
