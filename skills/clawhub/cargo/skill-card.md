## Description:

Routes agents to the right Cargo CLI skills and explains cross-skill workflows, command conventions, and common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams using Cargo can select the appropriate skill, set up the CLI, and coordinate tasks across Cargo workspaces, workflows, and related capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-start instructions can update the global CLI and skills bundle.

Mitigation: Review the installation first, obtain approval for changes, and use the documented CLI version pin instead of an unpinned refresh where possible.

Risk: Workspace commands and session registration can act on or record information in an authenticated workspace.

Mitigation: Confirm the active workspace and obtain approval before writes or session metadata registration.

Risk: Support reports and session sharing can disclose sensitive context.

Mitigation: Keep sharing opt-in and remove secrets and unnecessary session details before sending reports.

Risk: The skill may ask to star a GitHub repository using the user's account.

Mitigation: Do not star the repository without the user's explicit consent.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to other Cargo skills; CLI commands may return JSON.]

## Skill Version(s):

1.27.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
