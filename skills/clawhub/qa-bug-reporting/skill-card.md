## Description:

QA Bug Reporting helps testers, developers, and product teams create reproducible bug reports with clear prerequisites, reproduction steps, expected and actual results, impact assessment, root-cause hypotheses, and supporting attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and product teams use this skill to draft or improve bug reports when defects need precise reproduction details, environment context, evidence attachments, and impact assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bug reports may include logs, screenshots, network traces, order examples, payment examples, or other sensitive evidence.

Mitigation: Use sanitized test data and mask customer, financial, identity, and production information before sharing or attaching evidence.

Risk: Packet-capture or Bash examples may be unnecessary or inappropriate for some defects.

Mitigation: Run shell commands or capture network traffic only in controlled environments and only when that evidence is clearly needed for the report.

Risk: Root-cause hypotheses or impact assessments can mislead triage if they are not verified.

Mitigation: Label hypotheses clearly and confirm reproduction steps, environment details, and evidence before submitting the bug report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-bug-reporting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown bug report templates, structured checklists, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include reproduction evidence descriptions, log excerpts, screenshot notes, network trace notes, and sanitized attachment lists.]

## Skill Version(s):

1.7.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
