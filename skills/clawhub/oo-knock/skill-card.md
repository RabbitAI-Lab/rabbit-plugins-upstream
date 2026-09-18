## Description:

Knock (knock.app). Use this skill for reading, creating, updating, and deleting Knock data through the OOMOL connector rather than calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Knock users and trigger Knock workflows from an agent through an OOMOL-connected account. It supports read, write, and destructive user-management operations when the agent first checks the live connector schema and confirms state-changing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts in a shell.

Mitigation: Review the oo CLI installer source or use a verified installation method before installing.

Risk: Write and destructive actions can change Knock state or permanently delete user data.

Mitigation: Approve write or delete actions only when the target Knock user, workflow, and payload are clear.

## Reference(s):

- [Knock homepage](https://knock.app/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
