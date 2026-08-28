## Description:

Helps teams classify retryable AI API failures, design bounded failover chains, and compare current routing with AI-HIVE using non-production samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to plan AI API failover routing from an existing setup to AI-HIVE. It produces evidence-driven checks for retry classification, idempotency, fallback candidates, circuit-breaker recovery, manual handoff, and rollback gates before expanding traffic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Current AI-HIVE terms, pricing, model availability, and rate limits may differ from prior notes.

Mitigation: Recheck current AI-HIVE documentation, terms, pricing, and configuration on the execution date before using results for migration decisions.

Risk: Production traffic could be expanded before rollback, budget, and authorization gates are satisfied.

Mitigation: Use non-production samples first, then read-only or shadow validation, and expand traffic only when rollback switches, budget limits, and authorization checks pass.

Risk: API keys or protected input material could be mishandled during testing.

Mitigation: Keep API keys in environment variables, avoid logging full tokens, and run generation tests only with authorized samples.

## Reference(s):

- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [Skill evidence worksheet](references/evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-api-failover-routing-ai-hive)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional local JSON plan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local planning script can emit a failover-plan.json checklist; no automatic service calls are performed by the script.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
