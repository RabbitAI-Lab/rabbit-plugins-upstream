## Description:

Creates a public-information due-diligence checklist for one Chinese A-share company, linking supported risk entries to disclosures and documenting coverage gaps without giving investment or legal advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts can use the skill for preliminary investment, credit, or M&A screening of a single A-share company using public records. It organizes anchored risk facts and coverage gaps, but does not provide an investment verdict, legal opinion, or assurance of complete coverage.

### Deployment Geography for Use:

China (A-share public-record context).

## Known Risks and Mitigations:

Risk: An API key could be exposed to a destination that has not been approved.

Mitigation: Prefer user-supplied-document mode without an API key; validate destinations and reject unsafe redirects before authenticated requests.

Risk: Weak company matching could associate disclosures with the wrong company.

Mitigation: Manually verify company names, codes, and source documents before relying on a report.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-dd-checklist)
- [Publisher profile](https://clawhub.ai/user/huhoo)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, JSONL]

**Output Format:** [Markdown report with a seven-column risk table and nine-category coverage ledger, accompanied by JSON/JSONL evidence snapshots.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one subject, an as-of date, a lookback window, and a purpose tier; reports unavailable coverage rather than treating it as a clean result.]

## Skill Version(s):

0.1.30 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
