---
name: medication-information-research
description: Retrieve source-attributed GoodRx medication, condition, and health information with author and review dates, and cross-check safety-critical claims against official FDA or NIH sources. Use for general information, not personalized diagnosis, dosing, or treatment decisions.
allowed-tools: Bash(scripts/crawlora.sh:*)
---

# Medication information research

Build a concise, source-linked explanation from public GoodRx medication and
health pages. This workflow retrieves information; it does not diagnose, select
a medicine, recommend a dose, or decide whether a treatment is suitable for a
person or animal.

## Access and source limits

Set `CRAWLORA_API_KEY` and use the bundled `scripts/crawlora.sh`. It sends the
key to Crawlora over HTTPS, not to GoodRx or FDA. Check HTTP status and the
application `code`; stop on authentication errors, back off on `429`, and retry
a transient upstream failure once. Bound page requests to the user's question.
The selected routes are read-only. Do not submit medical or prescription data.

GoodRx is an editorial secondary source. Preserve its article URL, authors,
medical reviewers, and published/modified/reviewed dates where returned. GoodRx
states that clinically focused content is medically reviewed and that its site
is not a substitute for professional medical advice. Its editorial review does
not make a page an FDA-approved label. The REST helper returns JSON without HTTP
response headers, so it may not expose GoodRx's retained-response status. Keep
retrieval time separate from source review dates and do not claim that a fetch
was live. If current freshness is material, verify against the original page
and report any uncertainty.

## Find the right GoodRx material

1. Resolve the user-named medication or condition from the directory routes.
   Use `/goodrx/drugs` or `/goodrx/brands` for drug identity; `/goodrx/classes`
   and `/goodrx/class` for GoodRx's class directory; and `/goodrx/conditions`
   and `/goodrx/condition` for condition pages. A directory association is not
   a clinical recommendation.
2. For a drug guide, list `/goodrx/drug-guides` and use only a returned
   `slug`/`topic` pair with `/goodrx/drug-guide`. The supported topics are
   `side-effects`, `dosage`, and `interactions`; a missing guide is not a
   negative finding. Preserve the guide's reviewer, last-reviewed date, and
   source URL when present.
3. Use `/goodrx/drug-info` for the general medication page and its FAQs,
   warnings, contraindications, references, and comparison links. For pets,
   resolve the slug from `/goodrx/pet-medications` and set `audience=pets`;
   label veterinary content separately and do not transfer it to humans.
4. Use `/goodrx/health-topics` to discover a section/topic pair, then
   `/goodrx/health-articles` and `/goodrx/health-article` for a bounded article
   sample. Preserve author, medical reviewer, publication/modification dates,
   references, and article path. `/goodrx/answers` and `/goodrx/answer` provide
   GoodRx's short question-and-answer content; keep the question and linked
   article together.
5. Use `/goodrx/comparisons` and `/goodrx/comparison` only when the user asks
   how two named medicines are described. Preserve GoodRx's stated takeaways;
   do not turn a comparison into a treatment ranking or substitute choice.

## Verify claims and write the brief

- For dosage, contraindications, interactions, pregnancy, children, serious
  side effects, or other safety-critical claims, search official sources with
  `/web/search` using FDA, DailyMed, or MedlinePlus domains, then read the exact
  returned page with `/web/scrape` when available. Match the drug name, form,
  route, and product identity. FDA resources point consumers to FDA-approved
  patient labeling, Drugs@FDA, DailyMed, and NIH MedlinePlus; use GoodRx as an
  accessible secondary explanation, not as a replacement for those sources.
- If official material cannot be found or matched, label the point
  `GoodRx-only` or `not independently verified`. Do not bridge a missing
  population, formulation, or product with an assumption.
- Keep source statements separate from your plain-language summary. Preserve
  the exact source section, link, publication/review date, and retrieval time.
  A GoodRx list of condition-related medicines, FAQ, or alternative is not
  evidence that a drug is appropriate for a particular person.
- Do not give patient-specific dosing or interaction advice, advise starting,
  stopping, switching, or combining medicines, interpret symptoms, or replace
  a clinician/pharmacist. Refer those decisions to a qualified professional;
  urgent symptoms require local emergency help.
- Do not compare coupon prices in this skill; use
  `prescription-price-research` for user-requested price comparisons.

```sh
scripts/crawlora.sh /goodrx/drug-guides topic=interactions letter=t
scripts/crawlora.sh /goodrx/drug-guide slug=torsemide topic=interactions
scripts/crawlora.sh /goodrx/health-topics section=well-being
scripts/crawlora.sh /goodrx/health-articles section=well-being topic=sleep page=1 page_size=10
scripts/crawlora.sh /goodrx/health-article path=well-being/sleep/cbd-for-sleep
scripts/crawlora.sh -X POST /web/search '{"q":"FDA atorvastatin label interactions","include_domains":["fda.gov","dailymed.nlm.nih.gov"],"limit":5}'
scripts/crawlora.sh -X POST /web/scrape '{"url":"https://www.fda.gov/drugs/information-consumers-and-patients-drugs/find-information-about-drug","formats":["markdown"]}'
```

The deliverable should identify the question and population, summarize the
relevant GoodRx page and any official cross-check, link every source, retain
review/publication dates, and list unsupported or conflicting claims. A source
page or scraped summary is not a personalized medical answer.
