## Description:

深知可信搜索（法律、政策、标准） helps agents retrieve authoritative Chinese legal, policy, standards, public-service, subsidy, tax-benefit, and compliance materials through DKnownAI trusted search, with optional deep search when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and agents use this skill to search and verify Chinese legal, policy, standards, government-service, subsidy, tax, and compliance materials. The skill produces a sourced answer, clickable trace HTML, clean Markdown, and optional policy visualization artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The onboarding flow may share a phone number and SMS code with DKnownAI MaaS and temporarily handle a returned API key.

Mitigation: Run onboarding only when the user intends to create or access a DKnownAI MaaS account; never display the full API key; persist DKNOWC_API_KEY only after explicit user consent.

Risk: Endpoint override environment variables could redirect API-key-bearing requests to an unintended destination.

Mitigation: Use the default DKnownAI endpoints unless the runtime operator controls and trusts the override destination.

Risk: Search-backed legal, policy, or standards answers can become misleading if claims are unsupported, stale, or mismatched to the user's jurisdiction or facts.

Mitigation: Require source-backed citations for key claims, generate the trace HTML from the same final answer, and mark unsupported conclusions as requiring official confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-search)
- [DKnownAI publisher profile](https://clawhub.ai/user/dknownai)
- [DKnownAI MaaS platform](https://platform.dknowc.cn/)
- [Trusted search API endpoint](https://open.dknowc.cn/dependable/search)
- [Deep search API endpoint](https://open.dknowc.cn/api/services/deep-query/v2)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Direct answer text, clickable provenance HTML, clean Markdown, JSON search results, and optional self-contained visualization HTML or SVG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for live searches; generated files are expected under the skill's official-docs workspace.]

## Skill Version(s):

1.1.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
