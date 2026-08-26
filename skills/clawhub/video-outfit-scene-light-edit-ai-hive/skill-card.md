## Description:

Helps short-video creators, advertising post-production teams, apparel brands, and social media teams turn video outfit, scene, and lighting edit requests into reviewable production plans, AI-HIVE generation tasks, runnable commands, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, and developers use this skill to plan and execute video outfit, background, lighting, and generative edit workflows for ecommerce, advertising, social media, short drama, and product-promotion content. It emphasizes authorized source media, stable visual anchors, review before billable generation, and traceable AI-HIVE task records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and prompts may be sent to AI-HIVE when generation, upload, or chat commands are run.

Mitigation: Use only media the user is authorized to edit, review prompts and parameters before execution, and avoid submitting sensitive or unauthorized content.

Risk: AI-HIVE generation can be billable and may create duplicate charges during batch or retry workflows.

Mitigation: Confirm final parameters and routing before submission, start with small samples, and keep task records with input hashes and task IDs.

Risk: The skill uses an API key from the CLI, environment, or local configuration file.

Mitigation: Keep API keys out of logs, screenshots, and version control, and store local configuration with restricted file permissions on shared machines.

Risk: Generated edits involving people, brands, products, or uniforms may be misleading if authorization or facts are not verified.

Mitigation: Require authorization for source media and human review for identity, trademark, product, platform, and factual claims before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/video-outfit-scene-light-edit-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON snippets and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task records, model routing choices, price snapshots, media file paths, and local ffmpeg processing commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
