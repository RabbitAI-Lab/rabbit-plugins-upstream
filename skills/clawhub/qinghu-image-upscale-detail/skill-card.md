## Description:

Guides an agent through Qinghu AI's qhkit workflow to upscale and repair detail in one user-provided image while preserving the original content and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare qhkit commands for single-image upscaling, quote the required credits, submit the workflow after confirmation, poll for completion, and return generated image results. It is suited for product images, portraits, scenery, print-resolution preparation, and old-photo cleanup where content should not be restyled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a mutable third-party qhkit CLI and may direct agents to install or upgrade it globally.

Mitigation: Prefer a pinned, reviewed qhkit version and a local or isolated install before running workflow commands.

Risk: The workflow handles selected user images and may require a Qinghu API token and paid generation credits.

Mitigation: Get clear user confirmation before image upload or paid generation, use only authorized images, and store tokens through qhkit config or environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command and delivery guidance; qhkit status returns image URLs after the paid workflow completes.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
