## Description:

青虎AI 图片高清写实去 AI 感 helps an agent submit an image to Qinghu AI for fast realistic HD enhancement that reduces AI-looking artifacts, improves detail, and increases visual consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to enhance a single owned or authorized image through Qinghu AI, especially when an AI-generated image looks oily, distorted, blurry, or insufficiently realistic. The skill guides setup, quotation, submission, polling, and delivery of returned image options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs or upgrades the qhkit CLI and uses a Qinghu API token or configuration.

Mitigation: Confirm the user is comfortable installing qhkit and using Qinghu credentials before running commands.

Risk: The selected image is uploaded to Qinghu AI for processing.

Mitigation: Use only images the user owns or is authorized to process, and confirm external upload is acceptable.

Risk: The workflow is paid and may consume Qinghu credits.

Mitigation: Run the estimate step, report the returned credit cost, and wait for user confirmation before generation.

Risk: Ambiguous enhancement requests could trigger the wrong paid image workflow.

Mitigation: Confirm this specific realistic HD de-AI enhancement workflow is intended when the request is ambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Qinghu workflow log IDs, returned image URLs, status details, and final credit consumption when a paid workflow completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
