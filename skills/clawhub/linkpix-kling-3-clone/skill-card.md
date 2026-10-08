## Description:

Helps short-video creators analyze a reference video, adapt its structure to a product, and generate a new video with the Qinghu AI toolkit and an available Kling 3.0 model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video creators, editors, and ecommerce sellers use this skill to turn a reference video into a revised product-focused script and request an AI-generated promotional video. The workflow checks available models, estimates credits, and returns a link to the finished video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading Node.js and qhkit can change the local runtime environment and fetch packages at task time.

Mitigation: Review proposed installs and run them only in an environment where these changes are acceptable.

Risk: An API key provided for qhkit may be stored locally or exposed if pasted into chat.

Mitigation: Prefer a secret store or environment variable over sharing a long-lived key in chat, and review local credential storage.

Risk: Video generation can spend account credits.

Mitigation: Check the estimated credit cost and obtain user confirmation before submitting generation jobs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-kling-3-clone)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, Video links]

**Output Format:** [Markdown with commands, status updates, and output links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated and charged credits and links to completed media.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
