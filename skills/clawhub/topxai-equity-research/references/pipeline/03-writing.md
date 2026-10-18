# 3. Writing (the fixed chapter structure)

> This is steps 3 and 3.5 of the pipeline in `SKILL.md`. Previous step: `02-research.md`. Next step: `04-audit.md`.

**Source-file convention.** `research/<report-id>/parts/pNN-<chapter>.md` (primary language) and `parts/<lang>-pNN.md`
(second-language edition, if any) are the **only sources**. The assembled files (`<lang>.md`) are generated and **must never
be edited by hand**. To change a number, change the part and re-assemble. Front matter is written only at the start of
`p01`. Assemble with a small script of your own: concatenate the parts in filename order with a blank line between parts
(otherwise a heading directly after a table gets absorbed into the table), and resolve label placeholders such as
`[[t:label]]` and `[[f:label]]` into table and figure numbers, so inserting a table does not mean renumbering by hand.

**Company report structure: 16 chapters and 4 appendices.** Chapters 3 to 6 are the payload chapters and vary with the
subject. The three-horizon outlook, the price ladder, the decision chapter, the misreading section and Appendix D required by
`quality-bar.md` are never optional.

> 1. Summary and three-horizon outlook (business and funding structure / dashboard / core judgments / hypothesis track /
>    three-horizon outlook table and transition-condition box, which appear once in the whole report, here)
> 2. Business model and transmission chain (mechanism diagram and lags)
> 3. Contract ledger
> 4. Counterparties and financiers
> 5-6. Two cause-layer chapters (sites and power are always one; the other follows the subject, such as asset economics or the
>    structure of a counterparty's backing)
> 7. Financial quality (including the window-dressing checklist)
> 8. Capital structure and dilution
> 9. Governance and insiders
> 10. Peer mirror
> 11. Market-implied pricing (consensus reconstruction and E1-E5)
> 12. Valuation (two paths, the three-scenario price ladder, the basis for probabilities, a consistency reconciliation)
> 13. Operating framework (the five items of the decision chapter in `quality-bar.md`)
> 14. Risks (ordered by observability)
> 15. Misreading section
> 16. Tracking indicators, falsifiable conditions, catalyst path, and what to track over different holding periods
> - Appendix A: glossary and definitions
> - Appendix B: sources and known limitations (including the standing entries)
> - Appendix C: disclosures (from `assets/disclaimer.md`, verbatim), the audit revision log, and the version
> - Appendix D: derivations and calculations

The appendix split above is fixed. "16 chapters" is a working skeleton, not a hard count. Do not write an "operating
framework by investor type": it contradicts the disclaimer's "not directed at any particular investor". Write "what to track
over different holding periods".

**Industry reports**: the structure is in `references/industry.md` Step 8, with the three-horizon outlook, operating
framework and Appendix D of `quality-bar.md` added on top. Inside each link of the chain, use this order: primary numbers
anchored first, the core-judgment box, the definitions box, the vendor comparison table, then this link's data gaps.

**Valuation numbers have exactly one source**: `research/<report-id>/calc/model.py`. All inputs sit at the top, each marked
[A] for a filed value or [C] for an assumption. Run `python3 calc/model.py > calc/model-vN-output.txt`. Valuation numbers
in the body and in Appendix D come **only from that output file**. Never calculate them by hand.

**Required components**: the eight items in `framework.md` section 5 are mandatory: mechanism diagram, evidence grading,
certainty layering, bull/bear comparison, falsifiability and observation calendar, known limitations, misreading section,
audit revision log. Placement is in the structure above.

## 3.5 The tradable-judgment pass (before the draft is final)

Finishing the analysis is not the same as finishing the report. Go through `references/judgment.md` section by section:
consensus reconstruction (with its degrade path) -> mispricing evidence (E1-E5) -> **catalyst path table** -> rating basis
(12 months, benchmark and start date) -> the four decision items (three-scenario prices, risk/reward ratio, **invalidation
price**, time to realisation) -> evidence-strength binding -> the bear's three arguments answered one by one (step 2.5). The
result format and the added checks of the final review are in `judgment.md` section 9.

**This pass is what separates the report from commentary.** Without it, the report ends up with every number right,
every definition clear, and a reader who does not know what to do.

## Writing style

Write plainly. The audience is a professional reader scanning for the decision. Remove filler, hype and templated phrasing.
Make each heading a declarative conclusion that carries a number, and put the conclusion in the first sentence of each
paragraph. The three failure modes that appear most in research text:

- **Triplets**: three short sentences or items that share the same opening words. Cut to the one that carries the number.
- **Abstract nominal stacking**: "the implementation of the optimisation of ...". Use a verb and an object.
- **Closing flourishes**: a last sentence that lifts the paragraph to "the industry" or "the era". End when the claim ends.

The appearance-and-copy lane of the first-round audit checks the same list (`quality-bar.md` section 3, item 4).

## When several agents write chapters

Create `research/<report-id>/WRITING-CONTRACT.md` first (template: `assets/templates/writing-contract.md`). Its core rules:
numbers come only from `data-*.json` and `notes-*.md`; superseded values may appear only as a correction; an unresolved
conflict is written as `⟦OPEN: conflict N⟧` and no writer picks a version; no one smooths over an upstream contradiction;
no pipeline traces in the text; no buy or sell wording.

Run a mechanical gate on the assembled draft if you have one (a search for the forbidden-phrase list, leftover `⟦OPEN`
markers, numbers that appear in no data file). A gate that raises false alarms gets ignored. Tune it to zero false alarms
before you let it block anyone. Two typical false alarms: reading the word list inside a self-check comment block as a
match, and flagging a plain declarative heading that has no number.

## Pitfalls (collected from past work)

- **Numbers come only from the derivation file.** A second-round audit found an operating-basis figure off by nearly an
  order of magnitude: the number in a memo was wrong, and copying from the memo around the derivation file is a violation.
  The same round caught "contributes two thirds", which was really a weight; by contribution the share was far higher.
- **For every judgment sentence, ask whose debt this number subtracts.** A claim that the contracted portion "leaves no
  equity" had charged the construction cost of a later phase to the contracted portion's net debt. The attribution was
  wrong, and the opposing-side review caught it. The same accounting rule for cash is in `judgment.md` section 5.
