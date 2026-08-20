## Description:

This skill helps agents use the qhkit CLI to produce video storyboard scripts and storyboard images from product prompts and uploaded images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to generate storyboard scripts and storyboard images for video planning from product details and local image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit or Node can change the local toolchain.

Mitigation: Review install and upgrade commands before execution and run them only in an environment where toolchain changes are acceptable.

Risk: The skill can reuse an existing local qhkit/OpenClaw token and upload prompts or local image files to an external service.

Mitigation: Use only approved credentials and data, and confirm that external upload of the prompt and image assets is acceptable before generation.

Risk: Generated storyboard jobs may spend service credits.

Mitigation: Use qhkit estimate when cost matters and confirm sufficient balance before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, image URLs, guidance]

**Output Format:** [Markdown responses with qhkit CLI JSON command examples, storyboard script text, status updates, and generated storyboard image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, polling status, generated media URLs, and credit usage reported by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
