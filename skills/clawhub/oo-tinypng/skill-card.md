## Description:

Use TinyPNG (tinypng.com) through the OOMOL connector for image compression and output-image transformation requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate TinyPNG image compression and output-image transformation through an OOMOL-connected account. It helps agents inspect live connector schemas, run TinyPNG actions with JSON payloads, and handle setup errors when authentication, connection, or billing issues occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands.

Mitigation: Review and independently verify installer sources before running remote installation commands.

Risk: Image compression and transformation may upload image data and affect billing or service state.

Mitigation: Confirm the payload and intended effect before running TinyPNG actions, especially for user-provided images or billable operations.

Risk: The security evidence reports that the skill understates risks by treating image-processing actions as read-only.

Mitigation: Treat TinyPNG processing as an external write-like operation and review the skill before installation.

## Reference(s):

- [ClawHub TinyPNG Skill Page](https://clawhub.ai/oomol/skills/oo-tinypng)
- [TinyPNG Homepage](https://tinypng.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
