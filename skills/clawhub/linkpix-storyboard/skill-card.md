## Description:

Creates video storyboard scripts, shot plans, camera-movement suggestions, and storyboard images for product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to plan product videos as shot-by-shot scripts and generate accompanying storyboard images. It can provide a written storyboard and image prompts when image generation is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade qhkit and Node tooling on the user's machine.

Mitigation: Review the installation steps and prefer a preinstalled, pinned qhkit version.

Risk: Selected images and prompts are sent to the LinkPix/qhkit service, and an API token is required.

Mitigation: Share only approved materials and provide the token through a trusted secret mechanism, not a command or chat transcript.

## Reference(s):

- [LinkPix Storyboard skill listing](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images]

**Output Format:** [Markdown storyboard table and script, with generated storyboard images or image links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes shot timing, framing, camera movement, narration, and image prompts; images require a configured service token.]

## Skill Version(s):

0.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
