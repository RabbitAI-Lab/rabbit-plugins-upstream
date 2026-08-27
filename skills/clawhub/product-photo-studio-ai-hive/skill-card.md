## Description:

AI商品图工作室｜AI-HIVE helps ecommerce and marketing teams turn product-image requests into production briefs, prompts, AI-HIVE commands, generated image tasks, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, photography teams, designers, and multi-SKU operators use this skill to plan and produce product visuals such as white-background images, scene images, selling-point images, detail images, and platform-sized variants. Developers or operators can also run the bundled scripts to create JSON production briefs, query AI-HIVE models, upload authorized reference media, submit image generation tasks, poll task status, and download results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-selected media to AI-HIVE.

Mitigation: Use only product images, logos, videos, and other assets the user is authorized to provide to AI-HIVE.

Risk: The AI-HIVE script requires an API key and can store it locally during initialization.

Mitigation: Prefer environment variables or the provided init flow, keep the local config file private, and avoid placing secrets in prompts, logs, screenshots, or shared files.

Risk: Image generation requests can create billable AI-HIVE tasks.

Mitigation: Review prompts, model, routing mode, batch size, pricing snapshot, and output settings before submitting generation jobs.

Risk: Generated commercial product images may misrepresent product appearance, claims, endorsements, or platform compliance.

Mitigation: Validate product structure, colors, logos, text, authorizations, and claims against the provided facts before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-photo-studio-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs and generated media files; AI-HIVE generation calls require an API key and can submit billable tasks after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
