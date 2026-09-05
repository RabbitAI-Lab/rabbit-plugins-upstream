## Description:

DknownAI Trusted Search helps agents retrieve and verify authoritative legal, policy, standards, government-service, subsidy, tax, and compliance materials, then deliver a direct answer with clickable provenance HTML and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill for source-backed research on laws, policies, standards, government-service requirements, tax and subsidy programs, and compliance obligations. It is intended for tasks where answers need authority-backed citations, clickable provenance, and reusable Markdown output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy, legal, standards, and related query parameters are transmitted to dknowc services.

Mitigation: Use the skill only when the provider terms and retention practices are acceptable, and avoid sending sensitive personal, business, or legal facts.

Risk: Access provisioning may require a phone number and SMS verification when no API key is configured.

Mitigation: Review the onboarding flow before installing and use it only if phone verification is acceptable for the deployment context.

Risk: The agent handles an API key for remote service access.

Mitigation: Provide the key through the documented environment variable, avoid exposing the full key in chat or logs, and rotate or revoke it if mishandled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [DknownAI Trusted Search API](https://open.dknowc.cn/dependable/search)
- [DknownAI Deep Query API](https://open.dknowc.cn/api/services/deep-query/v3)
- [Search introduction reference](reference/search_intro.md)
- [Sample search result](reference/sample_search_result.md)
- [Sample trace report](reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Direct answer text, clickable provenance HTML, clean Markdown, JSON search results, and optional self-contained HTML visualization]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for live search; generated files are written under the skill workspace and delivered to the host workspace when available.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
