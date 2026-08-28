## Description:

Helps Amazon, TikTok Shop, independent-store, and overseas brand teams localize ecommerce content by turning product facts, target markets, platform requirements, brand voice, and prohibited claims into localized selling points, platform titles, image text, video scripts, and cultural risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce, marketing, and brand operators use this skill to convert product facts and authorized assets into localized content plans, copy, prompts, runnable AI-HIVE commands, and review checklists for cross-border ecommerce channels. It is intended for workflows where claims, reference materials, pricing, platform fit, and cultural risks need human review before publication or billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation tasks, routing choices, media uploads, and downloads are real account actions and may create cost or account impact.

Mitigation: Review prompts, model mode, routing, pricing snapshot, batch size, and command arguments before execution; start with a small sample before batch generation.

Risk: API keys or uploaded media could be exposed through careless configuration, logs, screenshots, or shared artifacts.

Mitigation: Use environment variables or the local config file with restricted permissions, keep keys out of prompts and committed files, and upload only assets the user is authorized to use.

Risk: Localized ecommerce content can become misleading if it invents product claims, live prices, platform outcomes, or user testimonials.

Mitigation: Ground selling points in supplied product facts and verifiable evidence, avoid guaranteed sales or ranking claims, and require human review for claims and platform compliance.

Risk: Reference-driven content may copy protected creative expression or imply unauthorized brand, person, or platform endorsement.

Mitigation: Use reference assets only when rights are confirmed; otherwise preserve only abstract structure such as information order, pacing, and evidence type while creating new wording and visuals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/cross-border-ecommerce-localization-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with runnable shell commands and optional JSON or generated media file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a local blueprint JSON file, upload authorized media to AI-HIVE, submit image or video generation tasks after confirmation, poll task status, and download generated assets.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
