## Description:

Browserbase (browserbase.com). Use this skill for ANY Browserbase request - reading, creating, updating, and deleting data. Whenever a task involves Browserbase, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Browserbase projects, sessions, contexts, and usage through an OOMOL-connected account without handling raw Browserbase API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running a remote installer script directly in a shell.

Mitigation: Install the oo CLI only through a verified, user-reviewed method, and avoid letting an agent execute the remote installer script without explicit approval.

Risk: Write and destructive Browserbase actions can create sessions, change contexts, delete contexts, or request early session release.

Mitigation: Confirm the exact action, target identifier, payload, and expected effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [Browserbase homepage](https://www.browserbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Browserbase connection](https://console.oomol.com/app-connections?provider=browserbase)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browserbase)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before building Browserbase action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
