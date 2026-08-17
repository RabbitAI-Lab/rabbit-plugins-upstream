## Description:

Provides NDA review, contract version comparison, legal citation checks, meeting brief generation, and status reporting to help legal teams process documents and identify risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Legal teams, legal operations staff, and authorized business users use this skill to triage legal documents, compare contract revisions, check citations, prepare meeting briefs, and assemble status reports. Outputs are decision-support materials and require review by a qualified lawyer before reliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive legal documents may be processed, written to files, logged, or sent through callbacks/API integrations with under-scoped authority boundaries.

Mitigation: Use only documents the user is authorized to process, restrict access, avoid administrator execution, confirm output and log locations, and review callback/API destinations before use.

Risk: Legal analysis, citation checks, current-law status, and privilege labels may be inaccurate or outdated.

Mitigation: Treat outputs as legal decision support only and have a qualified lawyer verify conclusions, citations, jurisdictional assumptions, and privilege determinations before reliance.

## Reference(s):

- [Legal Assistant Pro on ClawHub](https://clawhub.ai/thcjp/skills/legal-assistant-pro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, structured review tables, risk labels, citation notes, revision suggestions, privilege markings, action lists, and disclaimers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Often writes report files under output-specific paths; legal conclusions, current-law checks, and privilege labels require human legal review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
