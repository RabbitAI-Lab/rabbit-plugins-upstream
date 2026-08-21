## Description:

dknowc trusted search helps agents retrieve and verify authoritative legal, policy, government-service, standards, subsidy, tax-benefit, and compliance materials, returning sourced answers with clickable provenance and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill when an agent needs authoritative source retrieval for laws, policies, standards, government-service rules, subsidy or tax-benefit materials, and compliance checks. It supports direct answers backed by citations, clickable provenance HTML, clean Markdown, and optional policy visualization reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy, legal, standards, or compliance search questions are sent to dknowc's remote service.

Mitigation: Avoid entering confidential client, business, or personal details unless the provider's privacy and retention terms have been reviewed and accepted.

Risk: The skill includes phone-code onboarding to obtain an access key.

Mitigation: Review the onboarding step before use and do not proceed unless the user accepts phone verification for the remote service.

Risk: The skill can generate, reuse, or persist DKNOWC_API_KEY for future searches.

Mitigation: Approve key generation or persistence explicitly, avoid exposing the full key, and persist the environment variable only after user consent.

Risk: Security evidence says the skill understates that user questions are sent to the provider.

Mitigation: Disclose remote-service use in deployment guidance and review the skill before enabling it in workflows that may include sensitive legal, policy, or business queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [Skill README](artifact/README.md)
- [Search introduction and onboarding reference](artifact/reference/search_intro.md)
- [Sample trusted-search result](artifact/reference/sample_search_result.md)
- [Sample provenance report](artifact/reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON, Guidance]

**Output Format:** [Direct answer text with sourced Markdown, clickable provenance HTML files, clean Markdown files, JSON search results, and optional self-contained visualization HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for search execution; outputs are written under the skill's official-docs workspace when the skill runs.]

## Skill Version(s):

1.1.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
