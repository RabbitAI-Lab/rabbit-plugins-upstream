## Description:

Operate ElevenLabs account actions through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ElevenLabs connector schemas, run validated JSON requests, generate speech or sound effects, and manage voices, models, account details, subscriptions, and generation history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute unverified code on the user's machine.

Mitigation: Review installer instructions before installing and prefer an official, version-pinned OOMOL CLI installation method with checksum or signature verification.

Risk: Write and destructive ElevenLabs actions can change account state or delete generation history.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ElevenLabs homepage](https://elevenlabs.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elevenlabs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses and transit-storage references for generated or downloaded audio.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and artifact frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
