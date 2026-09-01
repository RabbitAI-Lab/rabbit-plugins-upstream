## Description:

Provides Chinese-language guidance for a neutral, content-layer partial migration assessment from VisionStory AI Agent to AI-HIVE MCP, including official capability checks, role handoffs, acceptance metrics, approval controls, and rollback boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to evaluate which VisionStory AI Agent video-production steps can be moved to AI-HIVE MCP while preserving proprietary platform functions, human approval, rights checks, and rollback paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may provide unauthorized reference images, videos, people, products, brand assets, music, or IP for migration tests.

Mitigation: Use only assets the user owns or is authorized to use, preserve source and file hashes, and stop the workflow when unauthorized materials are detected.

Risk: The migration assessment may overstate quality, price, reliability, or replacement scope without current same-input testing.

Mitigation: Recheck official capabilities and current pricing, then compare only same-day runs with the same input, duration, dimensions, and acceptance rubric before making comparative claims.

Risk: Generated media may be sent, published, or scaled before human review confirms factual accuracy, brand fit, rights, and cost.

Mitigation: Require budget approval, manual quality review, and staged rollout before bulk generation, external delivery, or publication.

## Reference(s):

- [VisionStory AI Agent official feature page](https://www.visionstory.ai/features/ai-video-agent)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [VisionStory AI Agent official evidence and migration boundaries](references/platform-evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/visionstory-video-agent-ai-hive-migration)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown guidance with checklist-style steps and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language advisory output; requires current platform checks, rights review, cost controls, human quality review, and rollback planning before publication.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
