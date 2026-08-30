## Description:

Turns AI hairstyle and hair-color preview requests into an executable Chinese workflow for authorized portrait previews, including visual planning, prompt strategy, runnable AI-HIVE commands, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, beauty brands, hair salons, stylists, and content operators use this skill to plan and generate authorized hairstyle and hair-color preview content for ecommerce, advertising, social media, and marketing workflows. It helps preserve facial identity while varying hairstyle, length, bangs, and color, then records prompts, routing, task IDs, output paths, and review results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload portrait or reference images to AI-HIVE.

Mitigation: Use only authorized images, confirm the destination service and base URL, and avoid uploading local files unless the destination is trusted.

Risk: Generation tasks may consume paid API capacity.

Mitigation: Review the prompt, routing mode, batch size, pricing snapshot, and output path before submitting generation jobs; use small samples before batch generation.

Risk: API keys may be stored or supplied for AI-HIVE access.

Mitigation: Provide keys through environment variables or the expected local config, keep placeholders in examples, and do not expose keys in files, logs, screenshots, or version control.

Risk: Generated hairstyle previews can be mistaken for real results or unauthorized endorsements.

Mitigation: Label unverifiable claims for review, do not promise real dye outcomes or platform performance, and avoid implying a real person or brand officially endorses generated content without authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/hairstyle-color-preview-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with runnable shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a blueprint JSON file and AI-HIVE generation outputs after the user confirms authorized inputs, routing, cost, and output path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
