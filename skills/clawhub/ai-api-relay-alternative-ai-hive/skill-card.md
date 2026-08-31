## Description:

Helps developers audit AI API relay usage and create AI-HIVE migration plans, routing choices, runnable examples, task ledgers, and acceptance checks for image and video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to compare an existing AI API relay or gateway with AI-HIVE, plan a low-risk migration, and produce Chinese-language checklists, sample commands, routing strategies, and validation criteria for media generation workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit billable AI-HIVE generation tasks.

Mitigation: Confirm model availability, pricing, routing mode, budget, and task scope before running generation commands; start with small non-production samples.

Risk: The scripts can upload local images, videos, or audio to AI-HIVE.

Mitigation: Use only media the user is authorized to upload and review applicable service terms, retention, privacy, and regional requirements before processing sensitive assets.

Risk: The init flow can persist an API key in ~/.ai-hive/config.json.

Mitigation: Prefer AI_HIVE_API_KEY environment variables for temporary use, keep local key files private, and delete ~/.ai-hive/config.json when persistent credentials are not desired.

Risk: The skill is configured for broad implicit invocation around AI API relay and model gateway topics.

Mitigation: Install only when AI-HIVE migration or generation assistance is intended, and review proposed actions before executing scripts.

Risk: Security evidence reports mismatched Token Hub identity strings in the artifact.

Mitigation: Review generated commands and script labels before reuse or publication, especially where names, model defaults, or routing examples affect user expectations.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)
- [Source and comparison boundary notes](artifact/references/platform.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-api-relay-alternative-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON files and runnable shell/Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit billable AI-HIVE API tasks, upload local media, download generated assets, and create local audit or blueprint JSON files when users run the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
