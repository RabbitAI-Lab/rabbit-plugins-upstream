## Description:

Helps AIGC, ecommerce, and advertising teams assess AI-HIVE as a WaveSpeedAI alternative and produce migration audits, compatibility checks, routing plans, runnable examples, task logs, and acceptance criteria for image and video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AIGC operators, ecommerce teams, and advertising teams use this skill to plan and test a migration or backup route from WaveSpeedAI-style media API aggregation to AI-HIVE. It produces structured migration inventories, capability maps, small-sample test plans, routing choices, task ledgers, and acceptance reports before production cutover.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local and network media workflows can upload user media and incur API costs.

Mitigation: Confirm current pricing and model availability before execution, use only authorized media, and start with small non-production samples.

Risk: The init flow can persist an AI-HIVE API key in ~/.ai-hive/config.json.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable, restrict local config permissions, and keep keys out of logs, screenshots, archives, and version control.

Risk: Broad implicit invocation can route ordinary API, image, or video questions into a vendor-specific migration workflow.

Mitigation: Disable implicit invocation or narrow trigger terms when the skill is installed in a shared or general-purpose agent environment.

Risk: Platform comparisons, prices, model availability, and stability claims can become outdated or misleading.

Mitigation: Use current provider documentation, contracts, same-input samples, and same-period billing evidence before recommending migration or production cutover.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/wavespeedai-alternative-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [WaveSpeedAI Reference Page](https://wavespeed.ai/seedance-2-api)
- [Platform Source and Comparison Boundary](references/platform.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with inline shell commands and generated JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local scripts for migration audits, media generation tests, and video processing; API credentials should be provided through environment variables.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
