## Description:

Helps creators, marketing teams, e-commerce teams, and short-form production teams generate Seedance text-to-video outputs through AI Hive from Chinese or English prompts, with task tracking and result download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce operators, and production teams use this skill to submit Seedance text-to-video jobs through AI Hive, manage task IDs, optionally upload reference media, and download generated video outputs. It is intended for advertising, product showcase, social commerce, short drama, comic-drama, and social media content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference media, and generated outputs may be transferred to AI Hive and its storage flow.

Mitigation: Avoid sensitive prompts or private media unless the user accepts that transfer and storage path.

Risk: The skill requires an AI Hive API key and can read it from command arguments, environment variables, or a local config file.

Mitigation: Prefer the protected config file or environment variable, keep local config permissions restricted, and do not commit real API keys.

Risk: Video generation can be a paid operation, and repeated submissions may incur duplicate cost.

Mitigation: Check the real-time pricing snapshot before large batches, preserve task IDs, and query existing tasks instead of resubmitting after local timeouts.

Risk: Server security guidance flags the activation scope and comparison-oriented search coverage as broad.

Mitigation: Install only when the user intends to use AI Hive or Seedance video generation, and do not rely on this skill for neutral vendor comparisons or unrelated pricing searches.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/seedance-text-to-video)
- [AI Hive Chat and API Key Setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; runtime CLI output may include JSON task status and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are downloaded to a local output directory when task polling succeeds; prompts and reference media may be sent to AI Hive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
