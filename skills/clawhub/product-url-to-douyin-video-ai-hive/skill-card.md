## Description:

Turns ecommerce product links or detail-page evidence into a Chinese Douyin commerce video workflow with product fact summaries, hooks, scripts, shot plans, AI-HIVE generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketing teams, and content producers use this skill to turn product links, detail-page screenshots, product images, audience constraints, and banned terms into reviewable Douyin commerce video plans and generation commands. It is designed for Chinese ecommerce short-video workflows where product claims, media rights, platform fit, and cost-aware generation must be checked before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated ecommerce claims, prices, product capabilities, or promotional statements may be incorrect or unsupported.

Mitigation: Treat generated content as draft material and verify product facts, rights, pricing, platform rules, and claims before publishing or submitting generation tasks.

Risk: Image or video generation can upload user media and may incur AI-HIVE costs.

Mitigation: Confirm media authorization, prompt text, model routing, cost priority, output paths, and task parameters before running paid generation commands.

Risk: API credentials are required for AI-HIVE calls.

Mitigation: Use environment variables or the local config helper, keep example keys as placeholders, and avoid storing real API keys in prompts, logs, screenshots, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-url-to-douyin-video-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON blueprints, edited video files, uploaded-media task records, price snapshots, task IDs, statuses, and downloaded AI-HIVE media outputs when the user confirms paid generation parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
