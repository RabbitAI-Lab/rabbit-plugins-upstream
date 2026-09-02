## Description:

Helps teams plan a controlled key and tenant migration from 柏拉图AI_API中转站 (api.bltcy.top) to AI-HIVE by mapping API key scope, subaccounts, project isolation, rotation windows, rollback gates, and evidence-based non-production tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering leads, and migration owners use this skill to inventory API keys, plan token rotation, compare current and target routing with non-production samples, and decide whether to cut over, hold, or roll back. It is focused on evidence-based migration planning rather than unsupported competitor claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may paste or store real API keys while planning the migration.

Mitigation: Use the skill for planning only, keep real keys in environment variables or approved secret stores, and never record plaintext credentials in generated plans.

Risk: Production key rotation or tenant migration could proceed without proper approval or rollback readiness.

Mitigation: Require explicit owner approval, verify rollback gates, and complete non-production shadow or small-sample tests before changing production traffic.

Risk: Platform terms, prices, routes, or model availability may change after the artifact was authored.

Mitigation: Re-check current platform documentation, terms, model lists, and price snapshots on the execution date before making migration decisions.

Risk: Unauthorized samples or unsupported claims could create compliance or reputational issues.

Mitigation: Use only authorized non-production samples and keep comparisons tied to same-time, same-input evidence rather than broad claims about either platform.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-api-api-bltcy-top-alternative-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [柏拉图AI_API中转站 (api.bltcy.top)](https://api.bltcy.top)
- [Evidence Sheet](references/evidence.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated JSON planning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper script creates a local JSON migration plan and does not call external services.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
