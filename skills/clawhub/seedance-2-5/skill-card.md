## Description:

Seedance 2.5 视频生成 helps creators, marketing teams, ecommerce teams, and short-form production teams generate or edit videos with AI Hive from text prompts and optional image, video, or audio references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce operators, and production teams use this skill to submit Seedance 2.5 video generation, reference-to-video, video editing, and extension jobs through AI Hive. It can upload supplied media, track task progress, and download generated video outputs for advertising, product demos, social content, short dramas, and comic-style video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running init stores an AI Hive API key on the local machine.

Mitigation: Run initialization only in a trusted environment, keep the config file private, and rotate or revoke the API key if it may have been exposed.

Risk: The skill can upload user-provided media to AI Hive and generated jobs may incur API charges.

Mitigation: Confirm that media is appropriate to upload and review routing, model parameters, and expected volume before submitting high-cost or batch jobs.

Risk: The discovery keywords are broader than the actual Seedance 2.5 video workflow.

Mitigation: Use the skill for AI Hive Seedance 2.5 video generation and avoid invoking it for unrelated competitor comparison or generic ecommerce research tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5)
- [AI Hive chat and API key access](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task responses; generated media is saved as video or image files by the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-provided media, return task IDs, poll task status, and download generated files to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
