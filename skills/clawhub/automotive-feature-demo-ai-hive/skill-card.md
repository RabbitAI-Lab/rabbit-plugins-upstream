## Description:

Helps automotive brands, dealers, media teams, and training teams turn vehicle feature demo requests into Chinese production briefs, scripts, AI-HIVE video generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Automotive brand, dealer, automotive media, and training teams use this skill to plan and generate feature-demo video workflows grounded in official vehicle facts, authorized media, platform constraints, budget, and review requirements. It produces reviewable Chinese briefs, storyboards, prompts, AI-HIVE commands, task records, and quality checks before any potentially paid generation step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads local automotive media to AI-HIVE and stores an AI-HIVE API key locally.

Mitigation: Use only authorized media, keep API keys out of prompts, logs, screenshots, and repositories, and install the skill only when AI-HIVE upload and local credential storage are acceptable.

Risk: Video generation can incur cost and may route through different AI-HIVE modes.

Mitigation: Review the generated command, routing mode, model configuration, and pricing snapshot before running generation, and use a small sample before batch work.

Risk: Automotive demos can create misleading feature, performance, safety, or comparison claims if source facts are incomplete.

Mitigation: Ground claims in official vehicle materials, mark unverified facts as pending review, and avoid unsafe driving scenes, unsupported feature claims, and unauthorized brand comparisons.

Risk: The skill allows broad implicit invocation for automotive video topics.

Mitigation: Review activation behavior during deployment and require human confirmation before commands that upload files, spend credits, or generate deliverables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/automotive-feature-demo-ai-hive)
- [AI-HIVE web app](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured sections, inline bash commands, JSON task records, and checklist items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local blueprint JSON paths, AI-HIVE routing choices, model IDs, pricing snapshots, task IDs, status output, and downloaded media file paths when commands are run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
