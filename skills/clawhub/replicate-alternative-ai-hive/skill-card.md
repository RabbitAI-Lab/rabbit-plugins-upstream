## Description:

Helps developers and content teams evaluate, audit, and safely test AI-HIVE as a Replicate-style migration or backup workflow for image, video, and batch content generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content operations teams, and marketing teams use this skill to inventory Replicate-like model API usage, map AI-HIVE capabilities, run small sample generations, record pricing and task evidence, and plan a phased migration with rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be provided through command-line arguments, environment variables, or a local AI-HIVE config file, and generation commands can trigger paid API usage.

Mitigation: Prefer environment variables, do not commit credentials, confirm budget before generation, and review or remove ~/.ai-hive/config.json after use.

Risk: Local images or videos may be uploaded during generation workflows, and source material or destination service terms may restrict use.

Mitigation: Confirm material rights and applicable service terms before upload or generation, especially for commercial content.

Risk: The skill may activate broadly for generic API, model-marketplace, image API, or video API questions.

Mitigation: Use it only for AI-HIVE or Replicate-style migration testing, and review generated plans before executing commands.

Risk: Model availability, pricing, limits, and service terms can change over time.

Mitigation: Query current AI-HIVE configuration and price snapshots at execution time, and avoid hard-coded cost or availability claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/replicate-alternative-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Replicate platform evidence page](https://replicate.com/bytedance/seedance-2.0)
- [Platform source and comparison boundary](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs and save local task or media files when the user supplies credentials and runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
