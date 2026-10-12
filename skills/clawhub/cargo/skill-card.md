## Description:

Routes agents to the right Cargo skill and explains how to coordinate CLI workflows, resource identifiers, and asynchronous jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market teams use this skill to select Cargo capabilities, set up a workspace, and coordinate multi-step CLI tasks across skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refreshing skills and global CLI tooling can change the installed environment from remote sources.

Mitigation: Review updates, prefer pinned versions, and skip refresh when the installation must remain unchanged.

Risk: Session registration and reports can transmit activity and troubleshooting details to Cargo.

Mitigation: Review reports before sending, exclude secrets and record-level data, and opt out of session registration when appropriate.

Risk: Some workspace operations require an admin token with elevated access.

Mitigation: Use an admin token only when the task requires it.

## Reference(s):

- [Cargo skill release](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo installation instructions](https://api.getcargo.io/INSTALL.md)
- [Prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [Common gotchas](references/gotchas.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes tasks to other Cargo skills; may suggest CLI commands and workflow sequences.]

## Skill Version(s):

1.27.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
