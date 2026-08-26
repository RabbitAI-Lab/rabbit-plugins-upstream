## Description:

Helps Xiaohongshu brands, creators, seeding teams, and lifestyle merchants turn product facts, authorized references, persona, scenes, titles, and brand colors into reviewable cover images, process images, detail shots, comparison images, prompts, commands, and delivery checklists while avoiding false testimonials or unsupported claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creators, e-commerce teams, and lifestyle merchants use this skill to plan and produce Xiaohongshu-style seeding image sets from confirmed product facts, authorized media, brand constraints, and platform requirements. It can also provide runnable AI-HIVE commands for image generation after the user reviews prompts, routing, and possible cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE image generation can be billable.

Mitigation: Review prompts, routing mode, model choice, and batch size before submitting generation tasks; start with a small sample before batch work.

Risk: Uploaded reference media may include content the user is not authorized to use.

Mitigation: Upload only media the user has rights to use, and fall back to abstract structure guidance when authorization is unclear.

Risk: Generated marketing images may imply unsupported product claims, false testimonials, platform outcomes, or official endorsement.

Mitigation: Keep claims grounded in confirmed facts, avoid fabricated certification or user experience, and require human review for regulated, personal, brand, or platform-sensitive content.

Risk: The AI-HIVE API key is required for API calls and could be exposed in logs or shared files.

Mitigation: Use environment variables or the local config file, keep placeholder keys in examples, and do not include real keys in prompts, logs, screenshots, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/xiaohongshu-seeding-image-studio-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional JSON files and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local blueprint JSON file and may submit AI-HIVE generation tasks only after user confirmation of prompts, routing, and potential cost.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
