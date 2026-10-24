## Description:

Image super-resolution tool: enhances image clarity and details, returning an enhanced URL, suitable for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to upscale low-resolution images for restoration or reuse and retrieve the enhanced image result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images are uploaded to dLazy for processing.

Mitigation: Only submit images that are approved for processing by an external hosted service.

Risk: Image processing may spend account credits.

Mitigation: Use the dry-run cost estimate and confirm the expected spend before processing.

Risk: The CLI stores an API key locally, and the skill depends on an external CLI.

Mitigation: Protect the saved key and review the CLI before installation; rotate or revoke the key if needed.

Risk: The example command uses --prompt while the listed image input option is --image.

Mitigation: Check dlazy superres -h and use the documented --image option for image input.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON result containing enhanced image URLs and metadata; optionally a downloaded image file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Enhanced images are hosted by dLazy; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
