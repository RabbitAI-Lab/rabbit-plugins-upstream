## Description:

Routes Cargo CLI requests to the appropriate skill and explains cross-domain workflows, setup, identifiers, polling, and common gotchas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this router to choose the right Cargo skill, prepare Cargo CLI commands, and coordinate work that spans multiple Cargo domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic software or skill updates may introduce changes that have not been reviewed.

Mitigation: Review and pin the CLI and skill source versions before installing or updating.

Risk: Session details may be uploaded without consistent prior approval.

Mitigation: Disable session uploads unless wanted, use scoped workspace access, and review what will be shared.

Risk: Diagnostic reports may include session details.

Mitigation: Require a redacted preview and explicit approval before sending a report.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills repository (metadata homepage)](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise task-oriented instructions; command examples may include placeholders for workspace-specific values.]

## Skill Version(s):

1.32.9 (source: skill frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
