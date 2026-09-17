## Description:

Use Formbricks through the OOMOL-connected oo CLI to read, create, update, and delete Formbricks data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Formbricks organization and workspace context, contacts, and contact attribute keys through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can direct an agent to run remote oo CLI installer scripts.

Mitigation: Install the oo CLI through a trusted, version-pinned, verifiable method before using the skill.

Risk: Write and destructive Formbricks actions can create, update, or delete workspace data.

Mitigation: Confirm the exact payload, effect, and target resource before allowing write or destructive actions.

## Reference(s):

- [ClawHub Formbricks skill page](https://clawhub.ai/oomol/skills/oo-formbricks)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Formbricks homepage](https://formbricks.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Formbricks connection page](https://console.oomol.com/app-connections?provider=formbricks)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON responses that include data and an execution identifier.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
