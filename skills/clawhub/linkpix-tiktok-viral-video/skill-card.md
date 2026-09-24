## Description:

Helps agents generate TikTok-oriented product and ad videos through LinkPix/qhkit, including model selection, asset upload, cost estimation, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketing teams, MCN operators, and ad specialists use this skill to create TikTok Shop, TikTok Ads, product seeding, multilingual talking-head, transformation, short drama, and feed-style promotional videos. The agent uses qhkit commands to inspect current model options, estimate cost, submit generation jobs, poll status, and return completed video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may require an API token for qhkit configuration.

Mitigation: Configure the token through a secure secret mechanism or environment variable where possible, and avoid exposing credentials in chat transcripts.

Risk: The workflow can install npm, Node, or Python tooling locally and may use unpinned latest package versions.

Mitigation: Preinstall or pin qhkit and related dependencies in a trusted environment before running generation tasks.

Risk: Product images, reference media, and prompts may be uploaded to the qhkit service for video generation.

Mitigation: Use only assets approved for external processing and review data-handling requirements before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-tiktok-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, credit estimates, status summaries, and external video URLs from the qhkit service.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
