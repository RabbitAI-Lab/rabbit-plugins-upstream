## Description:

Generates ecommerce video ad assets from product information for feed ads, brand promotion, and social media marketing, including multi-variant batch production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to prepare product video ad materials for short-video feeds, brand campaigns, and social channels. The skill guides an agent through qhkit-based estimation, user confirmation, task submission, polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit, Node/npm, Python image tooling, or related packages in the agent environment.

Mitigation: Prefer preinstalled and pinned dependencies; ask for user approval before persistent installs or upgrades and surface any installation errors clearly.

Risk: The skill may request or use a qhkit/LinkPix API key.

Mitigation: Use existing secure configuration or environment variables when available, avoid exposing tokens in conversation, and request credentials only when required.

Risk: Product images and prompts may be uploaded to the qhkit/LinkPix service for generation.

Mitigation: Confirm the user is comfortable sending the selected assets to the service and avoid uploading sensitive or unauthorized materials.

Risk: Generate commands can consume paid credits and submitted video tasks may not be cancelable.

Mitigation: Run estimates when supported, summarize model, count, orientation, language, inputs, and expected credits, then wait for explicit user confirmation before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, polling status, delivered video URLs, and quoted CLI error messages.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
