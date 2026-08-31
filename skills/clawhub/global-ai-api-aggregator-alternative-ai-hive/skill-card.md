## Description:

This skill helps teams evaluate AI-HIVE as an alternative AI API aggregator for Chinese ecommerce and generative media workflows, producing migration audits, routing plans, runnable examples, task ledgers, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce teams, marketing teams, and external evaluators use this skill to compare a current AI API gateway with AI-HIVE for text, image, video, editing, routing, and task-tracking workflows. It supports a cautious migration plan based on live model and pricing checks, non-production samples, gradual rollout, rollback conditions, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked implicitly for a vendor-specific AI-HIVE migration workflow.

Mitigation: Review the skill before installing or enabling implicit invocation, and invoke it only when an AI-HIVE evaluation or migration plan is intended.

Risk: The init flow can store an AI-HIVE API key in ~/.ai-hive/config.json.

Mitigation: Use environment variables when possible; if the config file is used, keep its permissions restricted and remove it when the workflow is complete.

Risk: Generation and upload commands can send prompts, images, videos, audio, or other media to AI-HIVE and may incur API charges.

Mitigation: Run samples with authorized non-production media, confirm budget and current pricing before execution, and avoid batch generation until the test plan is approved.

Risk: The skill exposes broader account and API actions than the short description makes clear, including user-info lookup, model listing, media upload, task polling, and result download.

Mitigation: Limit script execution to the specific command needed for the task and inspect command arguments before running account, upload, generation, or download operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/global-ai-api-aggregator-alternative-ai-hive)
- [AI-HIVE entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)
- [Source and comparison boundary](references/platform.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE API calls, upload authorized media, poll task status, download generated assets, and create local audit or blueprint JSON files when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
