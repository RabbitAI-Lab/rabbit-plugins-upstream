## Description:

ct-safety helps agents screen public FDA FAERS adverse-event data for drug-event safety signals using PRR, ROR, IC, and EBGM methods, with optional FDA label checks and China pharmacovigilance bulletin corroboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Pharmacovigilance, clinical-trial, medical, statistical, and regulatory users can use this skill to screen public adverse-event reports for potential safety signals, compare drug-event patterns, and produce auditable reports. Its outputs are screening evidence only and are not clinical, causal, prescribing, or regulatory decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports a mismatch between the declared no-hidden-logging posture and an AGENTS.md instruction to write persistent logs outside the output area.

Mitigation: Before installing or using the skill, remove or disable the auto-logging instruction, or require explicit user opt-in and keep any logs inside the selected output directory.

Risk: Drug-event signal reports from spontaneous adverse-event data can be misleading if treated as causal, clinical, prescribing, or regulatory conclusions.

Mitigation: Use outputs only as screening evidence and corroborate findings with qualified clinical or regulatory review, product labels, trials, and other appropriate evidence.

Risk: Case-level FAERS exports are public health data and may still be sensitive in aggregate or downstream use.

Mitigation: Use only non-confidential drug and event queries, limit detailed retrieval to confirmed analyses, and handle exported case files according to the user's data governance requirements.

Risk: The server security guidance calls out a pinned HTTP dependency that should be updated before routine use.

Mitigation: Review and update the pinned HTTP dependency during deployment maintenance before routine operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-safety)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/ct-safety)
- [openFDA drug event API](https://api.fda.gov/drug/event.json)
- [README](README.md)
- [Methods reference](references/methods.md)
- [FAERS fetch pipeline](references/fetch_pipeline.md)
- [Evidence hierarchy](references/evidence-hierarchy.md)
- [openFDA API key guide](references/openfda_api_key.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Conversational guidance plus generated HTML, XLSX, Markdown, JSON, CSV, and optional PNG report artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detailed retrieval and case-level exports require explicit user confirmation; case downloads are capped and written to the user-selected output directory.]

## Skill Version(s):

0.1.35 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
