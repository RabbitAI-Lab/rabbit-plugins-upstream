## Description:

v0 (v0.dev). Use this skill for ANY v0 request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and builders use this skill to operate v0 through an OOMOL-connected account for reading, creating, updating, deploying, and managing v0 chats, projects, environment variables, hooks, usage, billing, and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include pipe-to-shell remote installers that could execute changing external code on the user's machine.

Mitigation: Install the oo CLI through a trusted package manager or download and verify the installer before execution.

Risk: The skill can create, update, or delete v0 resources through an OOMOL-connected account.

Mitigation: Require live schema inspection plus explicit user confirmation for write and destructive actions before running the oo command.

Risk: Using the skill depends on OOMOL mediating access to the user's v0 account.

Mitigation: Confirm the user is comfortable with OOMOL-mediated account access and review the connected scopes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-v0)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [v0 homepage](https://v0.dev)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
