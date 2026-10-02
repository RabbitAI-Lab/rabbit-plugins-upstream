## Description:

Routes Cargo CLI tasks to the right skill and explains workspace setup, cross-skill workflows, and common operational pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market teams use this router to choose Cargo skills for account setup, workspace management, and multi-step workflows through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install and update hooks can make significant changes to the local CLI and skill bundle.

Mitigation: Review plugin hooks before use and prefer pinned versions to mutable updates.

Risk: Remote setup instructions and workspace commands may change or write to the wrong workspace.

Mitigation: Review remote setup steps and confirm the active workspace before making changes.

Risk: Reports and session shares can transmit commands, identifiers, errors, and workflow context.

Mitigation: Review report contents, omit secrets and sensitive records, and obtain consent before sharing session activity.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [Common gotchas](references/gotchas.md)
- [UUID flow](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authenticated account; actions may modify a workspace or spend credits.]

## Skill Version(s):

1.27.0 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
