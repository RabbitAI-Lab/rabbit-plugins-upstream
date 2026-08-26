## Description:

This skill helps agents use Qinghu AI to imitate a viral children's clothing video by uploading an authorized reference video and child model image, estimating paid credits, submitting the workflow, polling status, and returning generated media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, commerce operators, and agent users use this skill to create child-clothing promotional videos by transferring motion from an authorized reference video to an authorized child model image through Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media, including child imagery and reference videos, are uploaded to Qinghu AI.

Mitigation: Use only media the user owns or is authorized to process, confirm guardian authorization for child imagery, and disclose the upload before submission.

Risk: Submitting the generation workflow consumes paid Qinghu credits and task submission may not be cancelable.

Mitigation: Run the estimate first, summarize the selected workflow, fields, media, and expected credits, then wait for explicit user approval before generate.

Risk: The workflow requires local qhkit installation and Qinghu API token configuration.

Mitigation: Install the declared @iqinghu/qhkit package, keep credentials in qhkit config or QHKIT_TOKEN, and avoid exposing tokens in user-visible output.

Risk: Video quality and cost depend on the reference video length, clarity, and aspect-ratio match with the child model image.

Mitigation: Prefer short, clear, authorized clips, match image and video aspect ratios, and use the live options output rather than stale field names.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI console](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON snippets; qhkit command output is one-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs and a final Qinghu credits-consumed line after task completion.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
