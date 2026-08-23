## Description:

Routes ecommerce media requests to Qinghu AI qhkit workflows for video creation, image enhancement, watermark removal, model outfit changes, and short-video or creator data tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creators, and agent users use this skill to choose and run Qinghu AI workflows for product videos, ad creatives, image repair, watermark removal, outfit changes, and daily short-video or creator data tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived Qinghu API keys could be exposed if pasted into chat.

Mitigation: Set QHKIT_TOKEN or a local qhkit config file directly in the environment instead of sharing secrets in conversation.

Risk: The skill can route broad ecommerce media requests into a paid external Qinghu workflow.

Mitigation: Confirm the selected workflow, key parameters, uploaded media, and estimated Qinghu credit cost before running generate.

Risk: Selected local images, videos, or audio files may be uploaded to Qinghu during workflow execution.

Mitigation: Use only media the user owns or is authorized to process, and review file paths or URLs before submission.

Risk: Online workflow fields and prices may change after the artifact's August 2026 snapshot.

Mitigation: Run qhkit workflow options and estimate for the live workflow before submitting any job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit workflow command sequences, confirmation prompts for credit-consuming runs, status-polling guidance, final media URLs, and a credit consumption line when a paid task completes.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
