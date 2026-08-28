## Description:

Helps merchants and content teams turn e-commerce listing image requests into reviewable visual plans, prompts, runnable AI-HIVE commands, task records, and quality checks for product main images, white-background images, feature images, scene images, size images, and asset lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, marketing teams, and developers use this skill to plan and generate e-commerce listing image sets with authorized product facts, platform constraints, AI-HIVE routing, and delivery checks. It is intended for commercial listing-image workflows where users review parameters before any potentially billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call AI-HIVE with an API key and may submit potentially billable generation jobs.

Mitigation: Confirm prompts, model routing, batch size, price snapshot, and user approval before running generation.

Risk: The skill can upload user-provided reference media and download generated outputs.

Mitigation: Use only authorized media, avoid sensitive files, and confirm media rights before upload or generation.

Risk: API keys could be exposed through logs, screenshots, files, or repositories.

Mitigation: Use environment variables or the local config file, keep placeholders in examples, and avoid storing or sharing real keys in generated artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-listing-image-set-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat and API key entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON files or downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model routing, pricing snapshots, task IDs, generation status, local output paths, and acceptance checklist results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
