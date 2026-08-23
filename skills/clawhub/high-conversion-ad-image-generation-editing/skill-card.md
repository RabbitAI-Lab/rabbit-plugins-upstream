## Description:

Generates and edits ad image candidates with Nano Banana Pro through AI Hive, using funnel diagnosis, landing-page alignment, single-variable tests, and real-result review to support performance creative experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creative teams, and developers use this skill to generate or edit product and advertising image candidates for information-feed, display, ecommerce, and paid-social experiments. They compare one controlled visual variable at a time against funnel metrics and conversion results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, brand assets, and generated-task data leave the local machine for AI Hive cloud processing.

Mitigation: Use only assets you are authorized to submit, avoid confidential material, and review whether AI Hive is acceptable for the workflow before installation or use.

Risk: The init flow can store an AI Hive API key in a local configuration file.

Mitigation: Run init only when local key storage is intended, keep the file restricted to the current user, or provide the key through the environment for session-scoped use.

Risk: Generated ad images are conversion candidates, not guaranteed high-conversion assets, and may still need policy and claim review.

Mitigation: Treat outputs as test candidates, keep claims tied to approved evidence, review current platform policies before publication, and judge results with real funnel and conversion data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/high-conversion-ad-image-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task status from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally; prompts, reference images, brand assets, and task data are sent to AI Hive when the helper script is run.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
