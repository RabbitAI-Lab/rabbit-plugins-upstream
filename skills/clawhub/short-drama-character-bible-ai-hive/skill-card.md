## Description:

Short Drama Character Bible | AI-HIVE helps short-drama, comics, art, and AI video teams turn scripts and references into character cards, visual anchors, outfit changes, expression/action libraries, no-change constraints, and optional AI-HIVE image or video generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, and developers use this skill to plan short-drama character continuity, produce reviewable story and shot artifacts, and generate AI-HIVE image or video tasks only after parameters and possible costs are confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an AI-HIVE API key and may store a local key during initialization.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable, avoid committing keys, and review local configuration files before sharing logs or packages.

Risk: Selected local images, video, or audio may be uploaded to AI-HIVE for generation workflows.

Mitigation: Upload only media the user is authorized to use and confirm any privacy, likeness, trademark, or copyright constraints before submission.

Risk: Image and video generation may incur service charges.

Mitigation: Review prompts, model, routing mode, batch size, and price snapshot before running generation commands; use small samples before batch work.

Risk: Generated short-drama or marketing content can contain unsupported factual, product, or performance claims.

Mitigation: Require source-backed facts for product, finance, platform, and service-scale claims, and do not promise traffic, sales, ranking, approval, or return on investment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/short-drama-character-bible-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with runnable bash commands, JSON task records, and optional generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, upload user-selected media to AI-HIVE, poll asynchronous generation tasks, download generated media, and run deterministic ffmpeg edits.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
