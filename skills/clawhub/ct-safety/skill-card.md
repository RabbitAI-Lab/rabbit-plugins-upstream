## Description:

Screens FDA FAERS public adverse-event reports for drug-event pharmacovigilance signals using PRR, ROR, IC, and EBGM methods, with optional FDA label and China PV bulletin corroboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Pharmacovigilance, clinical-trial, and drug-safety professionals use this skill to screen public adverse-event reports for statistical safety signals and produce audit-friendly reports. Its outputs support signal triage and review, not clinical, causal, or regulatory decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party bug-report submission and auto-approved report egress may send sanitized diagnostic details outside the local environment.

Mitigation: Decline bug-report submission unless needed, review any description before sending, and avoid entering sensitive or identifiable details.

Risk: Stable hashed host or session identifiers and cross-session agent logging may create persistent local traces.

Mitigation: Review installation behavior before use and inspect or restrict local files such as ~/.workbuddy/AGENTS.md in controlled environments.

Risk: Case-level FAERS exports and generated reports may create local files containing detailed public adverse-event records.

Mitigation: Write outputs only to a controlled directory, limit case-level retrieval to necessary analyses, and manage generated files according to local data-handling policy.

Risk: Disproportionality outputs are screening signals and can be misleading if treated as causal, clinical, or regulatory conclusions.

Mitigation: Corroborate findings with product labels, trials, clinical context, and qualified pharmacovigilance or regulatory review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-safety)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage from metadata](https://github.com/medstatstar/ct-safety)
- [openFDA FAERS drug event API](https://api.fda.gov/drug/event.json)
- [Methods reference](references/methods.md)
- [FAERS fetch pipeline](references/fetch_pipeline.md)
- [Comparative FAERS design](references/faers-comparative-design.md)
- [Evidence hierarchy](references/evidence-hierarchy.md)
- [openFDA API key guidance](references/openfda_api_key.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, plus generated report files such as HTML, XLSX, JSON, Markdown, and optional PNG charts when the skill is run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detailed FAERS retrieval runs only after explicit confirmation or a direct-run request; case-level downloads are capped and outputs are written to the selected output directory.]

## Skill Version(s):

0.9.1 (source: server release metadata; artifact frontmatter reports 0.9.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
