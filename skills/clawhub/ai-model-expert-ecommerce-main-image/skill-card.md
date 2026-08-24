## Description:

AI大模型专家｜电商主图 helps e-commerce and marketing teams generate or edit commercial product images through AI-HIVE, with optional reference images, model routing, task polling, and result downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, product photography teams, brand marketers, and live-commerce teams use this skill to create product hero images, detail-page visuals, ad creatives, posters, social-commerce images, retouching, background replacement, and reference-guided visual variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit paid AI-HIVE generation jobs.

Mitigation: Confirm batch size, routing mode, and budget before running generation commands, especially for batch or high-cost jobs.

Risk: Local reference images may be uploaded to AI-HIVE.

Mitigation: Review each input image before upload and only use material the user is authorized to process through AI-HIVE.

Risk: The AI-HIVE API key is sensitive local configuration.

Mitigation: Store the key in the protected config file or environment variable, avoid pasting it into prompts or public files, and keep config permissions restricted.

Risk: Repeating a timed-out task submission may create duplicate paid jobs.

Mitigation: Save the returned taskId and query the original task instead of resubmitting after a timeout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-ecommerce-main-image)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; runtime output includes task IDs and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI-HIVE API calls for media upload, model lookup, task submission, task polling, and result download.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
