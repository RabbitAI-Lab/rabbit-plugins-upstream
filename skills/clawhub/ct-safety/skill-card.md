## Description:

Screens public FDA FAERS drug–event reports for potential safety signals using disproportionality measures and a safety signal score, with optional corroboration from drug labels and public safety bulletins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial safety teams, pharmacovigilance practitioners, and clinicians use this skill to screen public adverse-event reports and prioritize drug–event signals for expert review; results do not establish causality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drug and event search terms, plus a stable hashed device identifier, are sent to an external search service and may enable cross-session correlation.

Mitigation: Avoid confidential search terms; review the external-service disclosure and disable or replace the hardware-derived identifier if cross-session correlation is unacceptable.

Risk: The search destination can be changed through a CT_SEARCH_ENDPOINT environment override.

Mitigation: Check the configured endpoint before running searches and restrict it to an approved destination.

Risk: Sanitized bug reports can be transmitted to a separate external service.

Mitigation: Inspect the report and send it only after explicit user consent.

Risk: Adverse-event reporting biases and duplicate aggregate reports can make safety signals misleading if interpreted as incidence or proof of causation.

Mitigation: Treat outputs as screening evidence and require expert review and independent corroboration before clinical or regulatory decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/ct-safety)
- [Project homepage (listed in skill metadata; GitHub import provenance unavailable)](https://github.com/medstatstar/ct-safety)
- [Analysis methods](references/methods.md)
- [FAERS retrieval workflow](references/fetch_pipeline.md)
- [openFDA adverse-event data](https://api.fda.gov/drug/event.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Text or Markdown summary; optional HTML report and XLSX workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes disproportionality measures and optional signal scores; findings are screening signals, not causal conclusions.]

## Skill Version(s):

0.10.0 (source: frontmatter, ClawHub release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
