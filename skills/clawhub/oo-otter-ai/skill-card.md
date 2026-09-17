## Description:

Provides read-only Otter.ai access through OOMOL's otter_ai connector for listing conversations, channels, channel members, workspace data, conversation details, and temporary audio URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Otter.ai workspace, channel, member, and conversation data through an OOMOL-connected account without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The allowed oo CLI access can read Otter.ai workspace, member, transcript, and audio URL data through the connected account.

Mitigation: Use a least-privilege OOMOL and Otter.ai connection and review returned transcript, member, and audio URL data before sharing it.

Risk: The setup guidance includes pipe-to-shell installer commands.

Mitigation: Prefer official, versioned installation instructions with verification before installing or updating the CLI.

Risk: Temporary audio URLs and transcript details may expose sensitive meeting content.

Mitigation: Treat conversation details and audio URLs as sensitive outputs and limit retention, forwarding, and access to the intended audience.

## Reference(s):

- [ClawHub Otter.ai Skill](https://clawhub.ai/oomol/skills/oo-otter-ai)
- [Otter.ai Homepage](https://otter.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Otter.ai connector actions; temporary audio URLs may be returned for conversations.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
