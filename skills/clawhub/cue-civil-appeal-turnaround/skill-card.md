## Description:

Guides civil litigants preparing a second-instance appeal after an adverse first-instance judgment by analyzing the court’s reasoning, comparing evidence, organizing legal theories, and assembling filing documents; it does not provide legal advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Self-represented civil litigants use this skill to organize second-instance appeal preparation, including judgment analysis, evidence comparison, fact tracking, and draft filing documents. It is a workflow aid, not a substitute for legal advice or independent review of deadlines and legal arguments.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional online helpers may expose an API key or transmit confidential case materials.

Mitigation: Keep the core workflow offline unless online helpers are needed; verify the HTTPS destination and approve the materials to be transmitted.

Risk: The Word exporter may omit text from the source document.

Mitigation: Compare each exported Word document with its Markdown source before use or filing.

Risk: Legal arguments or deadlines may be incorrect or outdated.

Mitigation: Have deadlines and legal arguments independently reviewed before filing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-civil-appeal-turnaround)
- [Judgment reverse-engineering](references/01-judgment-reverse-engineering.md)
- [Evidence-diff protocol](references/02-evidence-diff-protocol.md)
- [Legal ladder](references/03-legal-ladder.md)
- [Fact ledger and discipline](references/04-fact-ledger-and-discipline.md)
- [Self-represented filing](references/05-self-represented-filing.md)
- [Document pack](references/06-document-pack.md)
- [Worked example](references/07-worked-example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown analysis tables, checklists, and draft filing documents; optional DOCX export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts require independent legal and deadline review; DOCX is an optional export.]

## Skill Version(s):

0.3.9 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
