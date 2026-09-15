## Description:

Bluesky enables agents to read, create, and update Bluesky data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to automate Bluesky profile lookup, timeline reading, post search, and text-post creation through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified remote installer script for the oo CLI.

Mitigation: Prefer installing the oo CLI from a verified release or package source with checksum or signature validation.

Risk: The create_text_post action changes state in the connected Bluesky account.

Mitigation: Confirm the exact post payload and expected effect with the user before running write actions.

Risk: The skill operates through an OOMOL-connected Bluesky account.

Mitigation: Connect only a Bluesky account the user is comfortable using through OOMOL and retry connection setup only after authentication or scope errors.

## Reference(s):

- [ClawHub Bluesky skill page](https://clawhub.ai/oomol/skills/oo-bluesky)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Bluesky homepage](https://bsky.social)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and can return JSON connector responses when run with --json.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
