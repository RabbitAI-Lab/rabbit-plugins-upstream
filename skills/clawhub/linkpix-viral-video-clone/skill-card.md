## Description:

Analyzes a Douyin or TikTok reference video link, reverse-engineers its script, and helps adapt the style, pacing, and shot structure into a similar product marketing video through LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creators, and agent operators use this skill to turn a reference Douyin or TikTok video into an adapted script and qhkit video-generation workflow for a product marketing video. The workflow is intended to preserve structure and rhythm while avoiding direct reuse of original materials or lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade unpinned qhkit tooling.

Mitigation: Install or upgrade only after explicit user confirmation and only when the user trusts the qhkit publisher.

Risk: The workflow may handle qhkit API credentials.

Mitigation: Prefer a scoped token supplied through an environment variable, and avoid persisting broad credentials in local config.

Risk: Video links, product images, prompts, and generated-task data may be sent to the LinkPix/qhkit service.

Mitigation: Confirm the user is comfortable sharing those inputs with the service before submission.

Risk: Reference-video cloning can create intellectual-property or attribution risk if original assets or wording are copied.

Mitigation: Adapt only structure, rhythm, and creative direction; do not reuse original materials or lines, and show the adapted script to the user before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include adapted scripts, task IDs, credit estimates, generated video URLs, and user-facing error messages returned by qhkit.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
