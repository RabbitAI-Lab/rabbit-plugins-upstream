## Description:

深知可信搜索（法律、政策、标准） helps agents retrieve and verify authoritative legal, policy, standards, compliance, subsidy, tax-benefit, and government-service materials through the dknowc trusted search service, then deliver answers with traceable source reports and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and agents use this skill to answer legal, policy, standards, government-service, compliance, subsidy, and tax-benefit questions with source-backed materials. It is suited for policy research, city policy comparison, enterprise subsidy or tax-benefit verification, and generating clickable verification reports plus clean Markdown deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends legal, policy, and standards research queries to the external dknowc service.

Mitigation: Use it only when users accept external trusted-search processing, and avoid submitting sensitive facts that are not needed for the query.

Risk: When no key is configured, the setup flow can ask for a phone number and SMS code to obtain an API key.

Mitigation: Explain the verification need before requesting contact information, do not expose full API keys, and persist credentials only after explicit user agreement.

Risk: Endpoint override options can redirect requests away from the default dknowc endpoints.

Mitigation: Use endpoint overrides only for destinations the operator fully trusts.

Risk: Generated reports are copied to a host workspace and visualization HTML may be opened locally.

Mitigation: Confirm where generated reports are copied, and avoid opening visualization HTML generated from untrusted structured data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-search)
- [ClawHub publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [MaaS management platform](https://platform.dknowc.cn/)
- [dknowc trusted search API](https://open.dknowc.cn/dependable/search)
- [Search capability reference](reference/search_intro.md)
- [Sample search result](reference/sample_search_result.md)
- [Sample trace report](reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, html, json, shell commands, configuration, guidance]

**Output Format:** [Direct answer text, clean Markdown, JSON search results, clickable HTML verification reports, optional self-contained HTML visualizations, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final answers are expected to bind key claims to returned source materials; optional visualizations should use already verified structured data with row-level source links.]

## Skill Version(s):

1.1.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
