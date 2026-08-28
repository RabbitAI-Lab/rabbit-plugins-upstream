## Description:

This skill helps ecommerce and marketing teams turn authorized virtual-host product-video requests into production briefs, scripts, prompts, runnable AI-HIVE commands, task records, and video acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators, private-domain marketers, cross-border sellers, and enterprise product teams use this skill to plan and generate virtual-host product-broadcast videos from authorized persona or product references, product facts, platform constraints, language, duration, and CTA requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real API keys or account credentials could be exposed in chat logs, screenshots, shell history, or repositories.

Mitigation: Use the AI_HIVE_API_KEY environment variable or the local config file, keep placeholders in shared examples, and avoid pasting real keys into prompts or source files.

Risk: Unauthorized reference media or persona likenesses could create copyright, privacy, or impersonation issues.

Mitigation: Use only assets the user is authorized to upload, and decline unauthorized replication, fake endorsements, or attempts to bypass platform rules.

Risk: Generated copy may contain outdated or unsupported product claims, prices, inventory, platform requirements, or legal conclusions.

Mitigation: Verify product facts, prices, inventory, platform rules, and legal constraints outside the model output, and mark unconfirmed facts as pending review.

Risk: AI-HIVE generation tasks may upload media and incur cost when submitted.

Mitigation: Review the prompt, selected media, model, routing mode, and pricing snapshot before generation; run a small sample before batch work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/virtual-host-product-video-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with scripts, prompts, checklists, JSON task records, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model routing choices, pricing snapshots, task IDs, media file locations, and ffmpeg processing commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
