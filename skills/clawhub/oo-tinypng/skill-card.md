## Description:

TinyPNG helps agents compress images from public URLs or base64 image data and transform TinyPNG output images through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run TinyPNG image compression and output-image transformation tasks through an OOMOL-connected TinyPNG account. It is intended for workflows that need schema-checked oo CLI commands and targeted setup recovery when authentication, connection, or billing issues block execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image-processing actions may send user-provided image data to TinyPNG/OOMOL.

Mitigation: Confirm the exact image payload and destination before running connector actions.

Risk: First-time setup includes remote installer commands.

Mitigation: Review installer sources independently before executing pipe-to-shell installation commands.

Risk: The skill under-labels image-processing actions even though they can create or transform remote image resources.

Mitigation: Treat compression and transformation actions as intentional data-processing operations and review payloads before execution.

## Reference(s):

- [ClawHub TinyPNG Skill](https://clawhub.ai/oomol/skills/oo-tinypng)
- [TinyPNG Homepage](https://tinypng.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before sending image payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
