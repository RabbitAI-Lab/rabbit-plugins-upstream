## Description:

Bird enables an agent to read, create, update, send, and delete Bird data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Bird contacts, channels, messages, and interactions from an OOMOL-connected account while relying on live connector schemas before submitting requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands download and execute code that can change outside this reviewed skill.

Mitigation: Review OOMOL's installer source or use a pinned, verified oo CLI installation method before running setup commands.

Risk: Write and destructive Bird actions can change or delete data in a connected Bird workspace.

Mitigation: Confirm the exact action, payload, expected effect, and target with the user before running write or delete actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oomol/skills/oo-bird)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Bird homepage](https://bird.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
