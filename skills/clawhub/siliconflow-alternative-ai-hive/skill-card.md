## Description:

Helps technical teams audit SiliconFlow-style AI API usage and build a cautious AI-HIVE migration plan with compatibility checks, routing choices, runnable examples, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical teams use this skill to compare current SiliconFlow or AI relay usage with AI-HIVE, prepare migration audits, generate small-sample image or video tests, and define rollback-ready acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation and vendor-specific recommendations may steer users toward AI-HIVE for generic AI API research.

Mitigation: Use the skill when the user intentionally wants an AI-HIVE-focused migration or sample-generation workflow; compare against current official platform documents and real test samples before switching.

Risk: Initialization and generation workflows can store an AI-HIVE API key under ~/.ai-hive/config.json and may incur generation charges.

Mitigation: Confirm credential storage, budget, routing mode, model selection, and billing expectations before running init or generate commands.

Risk: Image and video workflows can upload selected media to AI-HIVE or object storage.

Mitigation: Use only authorized non-production media for initial tests, verify retention and contractual requirements, and avoid uploading sensitive or unauthorized assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/siliconflow-alternative-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [SiliconFlow](https://siliconflow.com)
- [Platform comparison boundary](references/platform.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create migration audits, production briefs, task records, downloaded media, and ffmpeg-edited video files when users run the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
