## Description:

dknowc trusted search is a trusted search and authoritative-source retrieval Skill for policy, regulation, government-service evidence, standards, compliance, subsidy, tax-benefit, and policy research tasks that delivers direct answers, clickable provenance HTML, and clean Markdown without citation markers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and verify trusted legal, policy, government-service, standards, subsidy, tax-benefit, and compliance materials. It produces evidence-backed answers with clickable provenance HTML and clean Markdown, with deeper multi-round search only when explicitly requested or confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send searches, phone numbers, verification codes, and API key material to the dknowc service.

Mitigation: Review data-sharing expectations before installation and use it only when sending this information to the service is acceptable.

Risk: Endpoint override variables can redirect sensitive requests away from the default official hosts.

Mitigation: Use the default official endpoints and do not set endpoint or base override variables to unknown hosts.

Risk: Persisting DKNOWC_API_KEY in an untrusted environment can expose service credentials.

Mitigation: Persist the key only in a trusted environment and only after explicit user consent.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [DKnownAI publisher profile](https://clawhub.ai/user/dknownai)
- [dknowc MaaS management platform](https://platform.dknowc.cn/)
- [dknowc trusted search service](https://open.dknowc.cn/dependable/search)
- [dknowc deep search service](https://open.dknowc.cn/api/services/deep-query/v2)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, HTML files, clean Markdown files, JSON search results, SVG visualizations, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for service access and may generate local provenance HTML, clean Markdown, SVG, and intermediate JSON files.]

## Skill Version(s):

1.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
