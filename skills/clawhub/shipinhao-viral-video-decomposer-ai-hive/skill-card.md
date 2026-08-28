## Description:

Helps WeChat Channels operators, brand content teams, and ecommerce sellers decompose authorized viral short-video references into hooks, structure, rewritten scripts, storyboards, prompts, runnable AI-HIVE commands, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External video-channel operators, brand content teams, ecommerce sellers, and their supporting agents use this skill to turn an authorized reference video, product facts, target audience, and account positioning into a Chinese production workflow for original short-video content. It supports analysis, script and storyboard drafting, prompt generation, AI-HIVE task commands, task logging, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API use can involve paid image or video generation.

Mitigation: Confirm prompts, generation mode, routing mode, model, and price snapshot before submitting tasks; start with a small sample for batch work.

Risk: Media uploaded for generation or reference handling is shared with an external service.

Mitigation: Use only reference videos, product media, brand assets, and personal data that the user is authorized to upload and process.

Risk: API keys could be exposed through logs, screenshots, files, or repositories.

Mitigation: Use environment variables or local config, keep placeholders in examples, and do not echo real API keys in generated outputs.

Risk: Short-video decomposition could drift into copying protected expression, false product claims, fake testimonials, or platform-rule evasion.

Mitigation: Preserve only abstract structure, require factual support for claims, create visibly differentiated scripts and shots, and refuse unauthorized replication or deceptive claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/shipinhao-viral-video-decomposer-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated prompts, storyboard tables, task IDs, price snapshots, local file paths, and acceptance checklist results.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
