## Description:

ETF Intent Gate is a pre-dispatch gateway for ETF research platforms that filters unsafe or unsupported user input, classifies intent, rewrites allowed queries into objective research tasks, and routes or intercepts requests before downstream research agents run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nothingstop](https://clawhub.ai/user/nothingstop)

### License/Terms of Use:

MIT

## Use Case:

Developers and platform teams use this skill to add a front-door intent and safety gate to ETF or industry research workflows. It normalizes allowed research queries into downstream task context, blocks unsupported financial advice or injection attempts, and can route platform questions away from research agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw financial user queries may contain sensitive intent and are logged or retained in task context.

Mitigation: Restrict log access, configure retention and redaction rules, and avoid forwarding raw user queries beyond systems that require them for audit or debugging.

Risk: Runtime behavior depends on an OpenAI-compatible LLM provider selected through environment configuration.

Mitigation: Deploy only with an intentional provider configuration, protect INTENT_LLM_API_KEY, and review provider privacy terms before sending user queries.

Risk: Dependency ranges are not pinned to exact versions.

Mitigation: Use a locked dependency file or reproducible environment for production deployments and review dependency updates before release.

## Reference(s):

- [ETF Intent Gate ClawHub Release](https://clawhub.ai/nothingstop/skills/etf-intent-gate)
- [ETF Intent Gate Design](references/design.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, configuration]

**Output Format:** [Structured JSON responses and direct text replies for intercepted requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Forwarded task context includes request_id, standard_query, entity_extract, risk_warning, and agent_allow_list; intercepted requests return a direct user-facing reply.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
