## Description:

Helps Chinese short-drama, comics, virtual IP, and long-running content teams check serialized character continuity and prepare auditable AI-HIVE workflows, commands, and quality checklists for issue reports and optional media generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, and production operators use this skill to compare character bibles, previous episodes, current storyboards or videos, permitted changes, and timelines so they can identify continuity differences in appearance, clothing, props, voice, relationships, and chronology. When media generation is needed, it helps prepare AI-HIVE image or video commands, routing choices, task records, and review checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is assessed as suspicious because a narrowly named continuity-QA skill includes broad AI-HIVE upload and generation helpers with broad implicit activation.

Mitigation: Install and invoke it only for intended AI-HIVE continuity, media-generation, or production-workflow tasks, and review prompts, model choices, routing, and parameters before execution.

Risk: AI-HIVE media generation and batch tasks may create costs.

Mitigation: Show final prompts, parameters, routing mode, and expected task scope before submitting generation requests; use small samples before batch work.

Risk: The workflow can upload reference images, video, audio, or other production assets to AI-HIVE.

Mitigation: Upload only assets the user is authorized to send to AI-HIVE, and avoid confidential, private, infringing, or unlicensed material.

Risk: Initialization can store a local AI-HIVE API key file.

Mitigation: Prefer environment variables or protect the local config file, and ensure API keys are not committed, logged, screenshotted, or echoed back.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/serialized-character-consistency-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON, image, or video output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include continuity issue lists, evidence locations, severity labels, repair suggestions, AI-HIVE task IDs, routing choices, price snapshots, and downloaded media paths.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
