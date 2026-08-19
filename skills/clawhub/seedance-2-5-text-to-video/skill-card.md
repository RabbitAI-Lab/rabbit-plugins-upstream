## Description:

Seedance 2.5 文生视频 helps creators, marketing teams, e-commerce teams, and short-form drama teams generate video from Chinese or English text prompts through AI Hive, with task submission, status lookup, and finished-video download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, advertising and marketing teams, e-commerce operators, and content production teams use this skill to generate Seedance 2.5 text-to-video assets for ads, product showcases, social content, short dramas, and related campaign material. It also helps operators submit jobs, check task status, and retrieve generated video outputs from AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a stored AI Hive API key and submit cost-bearing video generation, upload, or task lookup requests.

Mitigation: Run it only after explicit approval for the intended generation, upload, or task lookup, and confirm the prompt, media, routing mode, and expected cost before submission.

Risk: The activation scope includes broad competitor, pricing, and tool-comparison search terms that may not require this API workflow.

Mitigation: Use the skill only for Seedance 2.5 generation workflows, not for general market research or comparisons unless a generation workflow is intentionally being prepared.

Risk: Prompts and approved media are sent to AI Hive and generated outputs are downloaded locally.

Mitigation: Avoid submitting sensitive, confidential, or unapproved media, and review local output files before reuse or publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-text-to-video)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API key and access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with command examples; CLI output may include JSON task data and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is downloaded to a local output directory unless the user chooses task submission only.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
