## Description:

Hybrid Catgirl is a dual-mode agent skill that switches between a professional technical assistant and the fictional multi-dialect catgirl roleplay character 猫猫.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ififi2017](https://clawhub.ai/user/ififi2017)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to give an agent a normal assistant mode plus an optional fictional catgirl roleplay mode with dialect switching, role reversal, and idle reminder behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional proactive reminder scripts store chat history and chat IDs.

Mitigation: Review the storage location and target chat configuration before enabling schedulers or messaging integrations.

Risk: Scheduled or messaging integrations may contact a configured chat unexpectedly if enabled without review.

Mitigation: Enable cron, scheduler, or messaging-platform integration only after confirming the platform permissions, schedule, and destination chat ID.

Risk: Roleplay chats may contain sensitive user input.

Mitigation: Do not paste secrets, API keys, or other credentials into roleplay chats.

## Reference(s):

- [Server-resolved source repository](https://github.com/ififi2017/hybrid-catgirl-skill)
- [ClawHub skill listing](https://clawhub.ai/ififi2017/skills/hybrid-catgirl-skill)
- [Environment Constraints Reference](https://github.com/ififi2017/hybrid-catgirl-skill/blob/bef8fc331ec868c07fa1bd8ee053eb33d2fb3fa1/references/environment-constraints.md)
- [寂寞小猫模式实现文档](https://github.com/ififi2017/hybrid-catgirl-skill/blob/bef8fc331ec868c07fa1bd8ee053eb33d2fb3fa1/references/lonely-cat-implementation.md)
- [Messaging Pitfalls](https://github.com/ififi2017/hybrid-catgirl-skill/blob/bef8fc331ec868c07fa1bd8ee053eb33d2fb3fa1/references/messaging-pitfalls.md)
- [Proactive Messaging Cost Control](https://github.com/ififi2017/hybrid-catgirl-skill/blob/bef8fc331ec868c07fa1bd8ee053eb33d2fb3fa1/references/proactive-cost-control.md)
- [Role Reversal Scenarios Reference](https://github.com/ififi2017/hybrid-catgirl-skill/blob/bef8fc331ec868c07fa1bd8ee053eb33d2fb3fa1/references/role-reversal-scenarios.md)
- [Hermes Agent](https://github.com/nousresearch/hermes-agent)
- [Hermes Agent catgirl skill blog post](https://ififi2017.github.io/posts/hermes-agent-catgirl-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Natural language and Markdown guidance with optional Python and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce roleplay responses and, when separately configured, proactive reminder message text.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
