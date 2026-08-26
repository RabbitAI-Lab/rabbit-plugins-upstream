## Description:

This skill turns authorized reference-motion short-video requests into production briefs, shot scripts, AI-HIVE video-generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce teams, and agent operators use this skill to plan and execute reference-motion transfer videos for dance, product, virtual-IP, social, advertising, and commerce content. It helps convert authorized source media and business constraints into a reviewable workflow, AI-HIVE task commands, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload selected prompts and media to AI-HIVE.

Mitigation: Use only media the user is authorized to upload and avoid sending sensitive or restricted content unless the user has approved that handling.

Risk: API keys may be supplied through the environment or persisted in ~/.ai-hive/config.json.

Mitigation: Keep API keys out of shared logs, screenshots, and repositories, and review the persisted config file after initialization.

Risk: Video generation can incur AI-HIVE charges after a task is submitted.

Mitigation: Confirm the final prompt, model mode, routing choice, and price snapshot before running billable generation, and use small samples before batch work.

Risk: Reference-motion transfer can be misused for unauthorized copying, likeness replication, or misleading commercial claims.

Mitigation: Require authorization for reference media and protected identities, preserve only abstract motion or structure when authorization is unclear, and mark unverified product or performance claims for review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/reference-motion-transfer-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce AI-HIVE task identifiers, pricing snapshots, local blueprint JSON, and downloaded media paths when generation is confirmed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
