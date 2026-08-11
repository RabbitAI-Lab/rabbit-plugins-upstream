## Description:

AI懂帮我巧匠 guides users through a conversational intake to create personalized AI profile, diagnosis, action-plan, and memory documents for configuring and refining an AI agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeasonhaitao](https://clawhub.ai/user/jeasonhaitao)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users use this skill when onboarding or refining a personal AI agent. It asks low-friction questions, summarizes user preferences and AI-use opportunities, and produces documents that can be copied into agent settings or kept as local records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated local documents can consolidate work details, preferences, memories, and confidential notes in plain Markdown or Word files.

Mitigation: Review and redact generated content before storing or sharing it, and delete files that are no longer needed.

Risk: The skill includes a SECRET.md workflow that could encourage users to place sensitive values into local files.

Mitigation: Do not put passwords, API keys, credentials, private client data, or other real secrets into SECRET.md.

Risk: The skill makes broad local-only privacy assurances that depend on the host agent and user environment.

Mitigation: Use it only in a trusted workspace and confirm storage and sync behavior before entering sensitive information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeasonhaitao/skills/ai-dong-bang-wo-qiaojiang)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational text plus Markdown and Word-style document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce AI profile booklets, AI enablement action plans, local memory files, behavior rules, and summaries for downstream agent configuration.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
