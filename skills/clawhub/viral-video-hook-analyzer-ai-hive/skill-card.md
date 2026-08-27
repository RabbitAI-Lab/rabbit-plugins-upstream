## Description:

A Chinese workflow for analyzing the first three seconds of commercial and social videos, then producing hook diagnostics, A/B-testable openings, scripts, prompts, runnable AI-HIVE commands, and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, editors, media buyers, and growth teams use this skill to analyze authorized reference videos or first-frame screenshots and turn product facts, audience pain points, and platform constraints into video-hook matrices, scripts, prompts, runnable AI-HIVE commands, and acceptance checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload user-selected media and run AI-HIVE generation tasks that may incur cost.

Mitigation: Review prompts, routing, model choice, expected cost, and media authorization before running generate commands.

Risk: API keys or generated task records could be exposed if copied into logs, screenshots, files, or version control.

Mitigation: Use placeholders in examples, provide secrets through environment or local config, and avoid sharing files or logs that contain credentials.

Risk: Reference-video analysis could be misused to copy protected material or make unsupported product claims.

Mitigation: Use only authorized reference material, preserve originality in characters, dialogue, shot design, music, logos, and watermarks, and require factual support for commercial claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/viral-video-hook-analyzer-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task IDs, model and routing selections, price snapshots, status records, and local file paths when generation is run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
