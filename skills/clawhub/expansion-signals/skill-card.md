## Description:

Helps customer teams identify renewal and expansion opportunities from won deals and dated public events, update account signals, and share a weekly Slack digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations teams and account executives use this skill to adapt a weekly customer-renewal workflow, identify expansion or at-risk signals, record reasons on accounts, and send an internal Slack digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public web content may influence customer judgments and account records.

Mitigation: Pilot on a few accounts, verify dated sources manually, and harden against prompt injection or disable web search when unsuitable.

Risk: The Slack digest includes customer names and renewal risk.

Mitigation: Set and verify an internal Slack channel before enabling the scheduled workflow.

## Reference(s):

- [Expansion plays example](references/expansion-plays.md)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Expansion Signals on ClawHub](https://clawhub.ai/cargo-ai/skills/expansion-signals)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions and TypeScript workflow resources; JSON account judgments and a Slack digest when deployed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates only the account's expansion signal, reason, and timestamp; the weekly digest summarizes flagged accounts.]

## Skill Version(s):

0.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
