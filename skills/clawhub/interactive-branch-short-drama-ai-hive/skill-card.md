## Description:

Helps short-drama teams, interactive content platforms, brand marketers, and gamified narrative creators turn authorized story inputs into branch trees, node scripts, character and scene boards, per-path video tasks, and continuity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and commercial content teams use this skill to plan interactive branch short dramas, generate reviewable production briefs, and prepare AI-HIVE image or video generation commands after confirming rights, platform constraints, and budget. Developers can also use the bundled scripts for deterministic blueprints, media generation task submission, task polling, downloads, and ffmpeg-based video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE media generation can be billable and can process user-provided prompts or media.

Mitigation: Confirm prompts, routing mode, budget, and task parameters before submitting generation jobs; start with a small sample for batch work.

Risk: The workflows require an AI-HIVE API key and may read, upload, edit, download, or write local media files selected by the user.

Mitigation: Keep API keys private, use environment variables or the local config flow, and pass only files and output paths intended for the task.

Risk: Generated scripts, claims, or branch choices could mislead audiences if source facts, rights, or platform limits are not verified.

Mitigation: Use only original or authorized materials, mark unverified facts for review, avoid fabricated endorsements or product claims, and run the continuity and rights checklist before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/interactive-branch-short-drama-ai-hive)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE Product Entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured checklists, JSON blueprints, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task IDs, routing choices, price snapshots, downloaded media paths, and continuity review notes when the user runs generation workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
