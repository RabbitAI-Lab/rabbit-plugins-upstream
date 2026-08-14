## Description:

Helps QA testers, developers, and teams create clear, reproducible bug reports with prerequisites, reproduction steps, expected versus actual results, attachments, impact assessment, and optional root-cause notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA testers, developers, and engineering teams use this skill to draft or improve bug reports so issues are reproducible, include the required environment and evidence, and can move into defect management with less back-and-forth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bug reports and attachments may include customer, identity, payment, screenshot, log, or production evidence.

Mitigation: Redact or mask personal, customer, financial, and production data before using the skill or sharing generated reports.

Risk: Examples mention packet capture and log inspection workflows that can collect sensitive operational data.

Mitigation: Run capture and log collection only in controlled test environments and review collected files before attaching them to reports.

Risk: Broad trigger wording may activate the skill during unrelated QA discussions.

Mitigation: Narrow trigger wording before publishing if accidental activation is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-bug-reporting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown bug report template, structured fields, examples, and checklist guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bug IDs, linked test case IDs, severity and priority, reproduction steps, expected and actual results, attachment lists, impact assessment, and optional root-cause notes.]

## Skill Version(s):

1.6.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
