## Description:

An offline Socratic reading companion that turns manually pasted passages into five questions, keeps reading notes in the browser, and supports user-confirmed cross-book comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Readers use the offline companion to reflect on passages they paste, save local notes, and confirm relationships between ideas from different books. It does not connect to a WeRead account or generate questions with an online model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved reading notes remain in that browser's localStorage until cleared and may contain sensitive text.

Mitigation: Avoid saving sensitive passages and clear the browser's site data when the notes are no longer needed.

Risk: User-downloaded Markdown or PNG comparison cards may include pasted copyrighted or sensitive passages.

Mitigation: Review exported content and share it only when authorized; use passages you have the right to use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [Usage and privacy FAQ](docs/faq.md)
- [Supported use cases](docs/canonical-cases.md)
- [GEO evaluation](docs/geo-evaluation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, PNG images]

**Output Format:** [Browser-based questions and notes; user-triggered Markdown or PNG comparison cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five deterministic questions per passage; notes persist in browser localStorage, while downloads require user action.]

## Skill Version(s):

1.4.4 (source: server-resolved ClawHub release; bundled documentation identifies 1.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
