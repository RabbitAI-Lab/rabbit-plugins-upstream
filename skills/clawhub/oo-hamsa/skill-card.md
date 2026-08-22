## Description:

Hamsa lets an agent search and read Hamsa project, voice agent, and TTS voice data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to query Hamsa project, voice agent, and TTS voice data through an OOMOL-connected account. The skill guides the agent to inspect the live connector schema before running read actions with the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Hamsa project, voice agent, and TTS voice data through the connected OOMOL account.

Mitigation: Install and connect the account only when that read access is expected, and use the documented live schema inspection before running actions.

Risk: CLI setup or account connection may be required before the skill can run Hamsa actions.

Mitigation: Follow the first-time setup steps only after an auth, connection, missing CLI, or billing error occurs.

## Reference(s):

- [Hamsa homepage](https://tryhamsa.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hamsa)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema output before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
