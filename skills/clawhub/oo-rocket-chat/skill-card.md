## Description:

Rocket.Chat enables agents to read, create, update, and delete Rocket.Chat data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Rocket.Chat through the OOMOL-connected oo CLI, including profile, room, and message reads plus guarded message posting, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells users to execute remote installer scripts directly in a shell.

Mitigation: Install only from trusted OOMOL distribution paths and prefer version-pinned installers with checksum or signature verification before running setup commands.

Risk: Rocket.Chat write and destructive actions can post, edit, or delete workspace content.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Rocket.Chat homepage](https://www.rocket.chat)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rocket-chat)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit JSON connector payloads and command results when Rocket.Chat actions are executed.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
