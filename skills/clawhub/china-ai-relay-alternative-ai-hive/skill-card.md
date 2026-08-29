## Description:

This skill helps Chinese-language business, ecommerce, marketing, and developer teams audit an existing AI relay or aggregation setup, evaluate AI-HIVE for image, video, advertising, and batch-generation workflows, and produce migration plans, runnable examples, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operations teams, and developers use this skill to plan and test a controlled migration from an existing AI relay or model aggregation platform to AI-HIVE, especially for image generation, video generation, ecommerce assets, routing choices, and batch production records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The AI-HIVE helper scripts can persist an API key to ~/.ai-hive/config.json.

Mitigation: Prefer AI_HIVE_API_KEY environment variables for routine use; if init is used, restrict the file to the local user and remove it when the key is no longer needed.

Risk: Image and video scripts may upload user-selected media, submit billable jobs, poll remote tasks, and download generated files.

Mitigation: Use only authorized, non-sensitive media for testing, confirm budget and routing before batch runs, and start with small samples before production traffic.

Risk: Security evidence notes bundled scripts that still identify a different Token Hub skill.

Mitigation: Publisher should correct the mismatched identifiers before broad use; users should review generated commands and configuration before running them.

Risk: Model availability, pricing, limits, and service terms can change.

Mitigation: Re-check AI-HIVE configuration, price snapshots, and applicable terms on the day of execution, and keep rollback paths for migration tests.

## Reference(s):

- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI endpoint](https://ai-hive.iclip.cn/api)
- [Source and comparison boundary](references/platform.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/china-ai-relay-alternative-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python examples, generated JSON audit files, generated JSON blueprint files, and media-generation task records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include AI-HIVE task IDs, model and price snapshots, local file paths, ffmpeg command output, and downloaded generated media when the user invokes the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
