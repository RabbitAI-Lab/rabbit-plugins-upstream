## Description:

Dknowc Trusted Search helps agents retrieve and verify authoritative Chinese legal, policy, standards, government-service, tax, subsidy, and compliance materials, returning sourced answers with clickable provenance reports and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and verify authoritative Chinese legal, policy, standards, government-service, tax, subsidy, and compliance materials. It supports sourced answers, policy research, city policy comparison, compliance evidence checks, and optional deeper multi-round verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone verification may create or retrieve an account/API key during onboarding.

Mitigation: Explain the verification step before use, request user consent for phone and code entry, never display full API keys, and persist keys only after explicit user consent.

Risk: Search queries are sent to the dknowc service.

Mitigation: Use the skill only when the user accepts the external search data flow, and avoid sensitive queries unless the user is authorized to send them.

Risk: Endpoint override environment variables can redirect requests.

Mitigation: Use the default dknowc endpoints unless the operator controls and trusts the override destination.

Risk: Security-review claims in the artifact should not be treated as proof of safety.

Mitigation: Use the server security evidence as authoritative and review the skill before deployment.

Risk: Legal, policy, and standards answers can mislead users if citations are stale, unsupported, or bound to the wrong source excerpt.

Mitigation: Require source-marker binding to retrieved materials, generate the provenance report from the same final answer, and downgrade unsupported conclusions to pending verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [Publisher Profile](https://clawhub.ai/user/dylanzhangzx)
- [Dknowc Trusted Search Endpoint](https://open.dknowc.cn/dependable/search)
- [Dknowc Deep Query Endpoint](https://open.dknowc.cn/api/services/deep-query/v3)
- [Dknowc Platform](https://platform.dknowc.cn/)
- [Search Introduction Reference](reference/search_intro.md)
- [Sample Search Result](reference/sample_search_result.md)
- [Sample Trace Report](reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, JSON, shell commands, configuration, guidance]

**Output Format:** [Direct answer text with sourced claims, clickable provenance HTML reports, clean Markdown without citation markers, and optional structured JSON or visualization files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured DKNOWC_API_KEY and sends search queries to dknowc service endpoints.]

## Skill Version(s):

1.1.6 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
