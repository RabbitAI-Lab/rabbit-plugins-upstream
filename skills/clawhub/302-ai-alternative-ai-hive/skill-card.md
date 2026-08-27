## Description:

This skill helps developers and teams assess and plan a controlled migration or fallback route from 302.AI-style OpenAI-compatible API relay usage to AI-HIVE for model API, image API, video API, ecommerce content, advertising, marketing, short-video, and batch-generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inventory an existing OpenAI-compatible relay setup, compare AI-HIVE fit for image and video generation workflows, create migration and rollback plans, run small samples, and produce task ledgers and acceptance criteria before any production switch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initialize and persist an AI-HIVE API key locally.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable for temporary use, and inspect or manage ~/.ai-hive/config.json if using the init command.

Risk: Image and video generation workflows may call paid remote APIs and download generated outputs.

Mitigation: Confirm model choice, routing mode, budget, and every paid generation task before execution; start with non-production samples.

Risk: Reference media can be uploaded to AI-HIVE during image or video workflows.

Mitigation: Use only authorized non-sensitive media until AI-HIVE terms, costs, retention, and data handling have been checked.

Risk: Migration recommendations may be misleading if based on stale model, price, or platform information.

Mitigation: Re-check current AI-HIVE and 302.AI documentation, contracts, availability, and same-day price snapshots before acting on any migration plan.

## Reference(s):

- [Platform Source and Comparison Boundary](references/platform.md)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [302.AI](https://302.ai)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/302-ai-alternative-ai-hive)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local audit, blueprint, media generation task, and video-editing artifacts when the included scripts are run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
