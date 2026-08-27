## Description:

Helps AI platform operators, enterprise developers, content studios, and ecommerce teams organize authorized model APIs behind an AI-HIVE relay with key isolation, routing, quotas, audits, and image/video task checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AI platform operators, enterprise engineering teams, content studios, and ecommerce technical teams use this skill to plan and test an authorized AI API relay workflow for model catalogs, credential isolation, routing, quotas, audits, asynchronous image/video tasks, cost snapshots, and result retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API calls may be billable and may upload user-selected media.

Mitigation: Use the skill only with an authorized AI-HIVE API key, review prompts and media before execution, and check cost snapshots before submitting generation tasks.

Risk: The helper can store an API key in a local configuration file.

Mitigation: Prefer environment variables or a protected local config, keep file permissions restricted, and rotate or revoke keys if exposure is suspected.

Risk: Sensitive or unlicensed files could be uploaded if users provide them as media inputs.

Mitigation: Upload only media that the user is authorized to process and avoid sensitive, confidential, or unlicensed content.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-ai-api-relay)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON blueprint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local JSON briefs, local credential configuration, AI-HIVE API calls, task IDs, cost snapshots, and downloaded media outputs when users execute the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
