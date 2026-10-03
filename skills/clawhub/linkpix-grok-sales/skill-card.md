## Description:

Grok 电商带货视频 | LinkPix helps cross-border sellers and content teams create social-commerce product videos through the qhkit/青虎 AI workflow, including model lookup, media upload, cost estimation, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, content teams, and agent operators use this skill to turn product images and selling points into short social-commerce videos for platforms such as TikTok, Instagram Reels, Douyin, Xiaohongshu, Amazon, and Shopee. It guides the agent through qhkit setup, model selection, parameter confirmation, paid generation, status polling, and video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can request an API key and may expose sensitive credentials if they are pasted into chat.

Mitigation: Configure credentials through a local environment variable or secret store, and avoid sharing raw API keys in conversation.

Risk: The workflow can install and run persistent qhkit command-line tooling.

Mitigation: Install only from the expected @iqinghu/qhkit package source, verify the package and version before use, and run it in an environment appropriate for third-party tooling.

Risk: Video generation can upload product media and spend credits.

Mitigation: Confirm model, duration, orientation, input media, and estimated credits before running any generation command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-grok-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit commands, setup steps, confirmation summaries, task IDs, status updates, and final video URLs.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
