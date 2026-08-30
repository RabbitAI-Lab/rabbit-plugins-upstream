## Description:

This skill helps Douyin shop, product-card operations, and Qianchuan advertising teams turn product facts, authorized assets, and campaign constraints into product-card image briefs, prompts, runnable AI-HIVE commands, variants, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce operators, advertisers, and developers use this skill to plan, generate, and review Douyin product-card imagery through AI-HIVE while preserving product accuracy, asset authorization, and mobile readability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can involve paid API usage and asynchronous downloads.

Mitigation: Review prompts, routing mode, model configuration, and price snapshot before submission; start with a small batch before scaling.

Risk: The workflow uses user-provided API credentials and may upload selected media.

Mitigation: Use an AI-HIVE API key scoped for this workflow, avoid storing keys in prompts or logs, and upload only assets the user is authorized to use.

Risk: Product-card imagery can mislead users if claims, endorsements, or reference material are not verified.

Mitigation: Confirm product facts, platform constraints, asset rights, and approval requirements before generation and before publishing outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/douyin-product-card-image-studio-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; helper scripts can produce JSON briefs, task records, and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation commands may upload authorized media, use AI-HIVE API credentials, poll asynchronous tasks, and download outputs when the user runs them.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
