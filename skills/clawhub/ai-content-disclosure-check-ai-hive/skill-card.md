## Description:

帮助广告主、内容平台、品牌法务和 AI 创作团队检查 AI 生成内容披露要求，并生成披露元素、标识位置、元数据台账、发布前检查表和可运行 AI-HIVE 命令。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, brand legal teams, content platforms, advertisers, and AI production teams use this skill to review AI-generated or synthetic media disclosure needs for ecommerce, advertising, marketing, short-video, comic-video, social selling, and seeding workflows. It produces a reviewable disclosure plan before any potentially billable AI-HIVE image or video generation task is submitted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can upload user-provided media to a remote service and may create billable image or video tasks.

Mitigation: Review prompts, files, routing mode, model choice, price snapshot, and output paths before running commands; use only authorized, non-sensitive reference media.

Risk: API keys may be supplied through environment variables, command-line flags, or a local ~/.ai-hive/config.json file.

Mitigation: Prefer environment variables for temporary use, do not paste real keys into shared logs or source files, and verify any persisted config file is protected.

Risk: Generated disclosure guidance may be incomplete because platform and legal rules change over time.

Mitigation: Check current official platform or legal requirements and keep human review for legal, brand, product, person, privacy, copyright, medical, financial, or child-related claims.

Risk: Downloaded media and ffmpeg edits write files to local output paths and can overwrite explicitly requested outputs.

Mitigation: Inspect output directories and filenames before execution, preserve originals, and run deterministic video edits on copies when source preservation matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-content-disclosure-check-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown with checklists, task records, prompts, JSON blueprints, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model or price snapshot, taskId, status, output file paths, and review or retest notes when generation tasks are used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
