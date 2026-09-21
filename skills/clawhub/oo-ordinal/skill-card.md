## Description:

Ordinal (tryordinal.com). Use this skill for ANY Ordinal request - searching and reading data. Whenever a task involves Ordinal, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Ordinal workspace data through an OOMOL-connected account, including ideas, posts, labels, users, engagement profiles, scheduling profiles, and workspace details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands run directly in a shell.

Mitigation: Install the oo CLI from verified OOMOL documentation yourself, and require explicit approval before an agent runs remote installers or authentication flows.

Risk: Connector calls depend on the live Ordinal action contract and the user's OOMOL connection state.

Mitigation: Inspect the live connector schema before building payloads and run setup or reconnection steps only after a matching command failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ordinal)
- [Ordinal homepage](https://www.tryordinal.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and focuses on read-only Ordinal get and list actions.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
