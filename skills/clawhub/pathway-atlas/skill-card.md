## Description:

PathwayAtlas guides students, families, and teachers through evidence-based Chinese gaokao planning across schools, majors, admissions pathways, and next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sarry12227](https://clawhub.ai/user/sarry12227)

### License/Terms of Use:

MIT

## Use Case:

Students, families, teachers, and advising agents use this skill to collect an anonymous planning profile, research public admissions evidence, compare school and pathway options, and produce practical next steps for Chinese gaokao planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install or update instructions may pull from a mutable repository during a consultation.

Mitigation: Install only from a trusted, pinned release or a verified ClawHub package, and avoid self-updating the skill while advising a user.

Risk: Large or untrusted PDF/XLSX attachments may expose the host to document parsing risk.

Mitigation: Process untrusted documents in a constrained environment and prefer verified public sources when available.

Risk: Education planning conversations can invite unnecessary personal data collection.

Mitigation: Do not provide real names, phone numbers, addresses, credentials, private local paths, or other sensitive identifiers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sarry12227/skills/pathway-atlas)
- [README](README.md)
- [Data Sources and Redistribution Policy](DATA_SOURCES.md)
- [Quick Planning](references/quick-planning.md)
- [Source Policy](references/source-policy.md)
- [Host Workflow](references/host-workflow.md)
- [Conversation Output](references/conversation-output.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown reports with optional code or shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce optional report files such as Markdown or DOCX when the host supports file output; admissions guidance is source-bound planning support, not an admission guarantee.]

## Skill Version(s):

0.2.5 (source: evidence release and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
