## Description:

Turns user-designated Chinese chat logs, meeting notes, and project updates into evidence-traceable collaboration status cards when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yamyeed](https://clawhub.ai/user/yamyeed)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and project teams use the skill to organize explicitly supplied Chinese collaboration records into structured status cards covering confirmed decisions, owners and deadlines, risks, blockers, dependencies, and items needing confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive details may be extracted before redaction, and redaction may be incomplete.

Mitigation: Remove secrets before providing records and review the result before sharing.

Risk: Reusing an output path with replacement enabled may overwrite a local file.

Mitigation: Specify exact input and output paths, and use --force only when replacement is intended.

## Reference(s):

- [Office Collaboration Radar on ClawHub](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)
- [Office Collaboration Radar (English)](https://clawhub.ai/yamyeed/skills/office-collaboration-radar-en)

## Skill Output:

**Output Type(s):** [JSON, Markdown, SVG, CSV]

**Output Format:** [Structured JSON status cards, with optional Markdown, SVG, and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven fixed modules; key conclusions include brief evidence excerpts, and missing or conflicting details are marked for confirmation.]

## Skill Version(s):

0.4.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
