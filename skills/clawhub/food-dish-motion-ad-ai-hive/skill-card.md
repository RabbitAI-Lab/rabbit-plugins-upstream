## Description:

Creates production-ready Chinese workflows for food and restaurant motion ads, including briefs, shot scripts, prompts, runnable AI-HIVE commands, task records, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, restaurant operators, food e-commerce teams, and local-life marketers use this skill to turn authorized dish assets and campaign facts into food-ad production plans, video prompts, AI-HIVE generation commands, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation may incur charges and upload user-selected media.

Mitigation: Review prompts, mode, routing, and media before submitting generation tasks; run small samples before batch work.

Risk: The skill can store an AI-HIVE API key locally during initialization.

Mitigation: Use environment variables or the generated config file with restricted permissions, and never commit keys, logs, or screenshots containing secrets.

Risk: A custom API base URL could direct prompts, keys, or media to an untrusted endpoint.

Mitigation: Use the default AI-HIVE endpoint unless the alternative endpoint is explicitly trusted.

Risk: Food, brand, or reference assets may be unauthorized or misleading.

Mitigation: Use only authorized assets and mark unverified claims, prices, store details, and product facts for human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/food-dish-motion-ad-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with runnable shell commands, JSON task records, and optional local media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON, AI-HIVE task records, downloaded generated media, and ffmpeg-edited video files.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
