## Description:

This skill helps accounting-firm marketers and operators create Chinese image, short-video, and content-marketing plans, prompts, task records, and AI-HIVE generation workflows while enforcing factual, authorization, budget, and professional-review boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams, agency operators, and accounting-firm staff use this skill to plan and produce reviewable Chinese marketing assets for accounting services, including audience strategy, a 30-day content calendar, image and video prompts, platform rewrites, AI-HIVE task records, and post-campaign review notes. Developers and technical operators can also use the bundled scripts to create local briefs, submit AI-HIVE image or video jobs, upload authorized media, poll task status, download outputs, and run deterministic ffmpeg edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded reference files are sent to AI-HIVE during generation workflows.

Mitigation: Use only authorized media, remove sensitive client or firm information unless sharing is approved, and review each prompt and upload before submission.

Risk: Image and video generation can incur API costs or use an unintended routing profile.

Mitigation: Confirm budget, model routing, and price snapshots before running generation tasks, and record task IDs for audit and retry control.

Risk: Marketing content for accounting services can contain unsupported claims about clients, cases, qualifications, tax savings, hiring, or project outcomes.

Mitigation: Require human review of all facts, credentials, client references, professional conclusions, and platform compliance before publication.

Risk: AI-HIVE API keys may be exposed if copied into project files, screenshots, logs, or version control.

Mitigation: Keep credentials in environment variables or a protected local config, avoid printing secrets, and exclude credential files from shared artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/industry-accounting-firm-marketing-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)
- [会计事务所图片视频内容营销行业手册](references/industry-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown guidance with bash commands and JSON task records; scripts can also write JSON briefs and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided AI-HIVE credentials for network generation tasks; deterministic brief generation and ffmpeg edits can run locally when dependencies are installed.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
