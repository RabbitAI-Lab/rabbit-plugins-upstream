## Description:

AI-powered domain naming consultation that helps users turn a vague project idea into candidate registrable domain names through a guided conversation and DomainKits availability checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abtdomain](https://clawhub.ai/user/abtdomain)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to clarify a project concept, explore brand-name directions, and check domain acquisition options with DomainKits before choosing a name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share sensitive launch plans or business details while asking for domain ideas.

Mitigation: Share only the details needed for naming and avoid confidential strategy, customer, or launch information.

Risk: API keys may be exposed if pasted into chat or configuration text.

Mitigation: Use platform-managed connector authentication or environment secret handling for DOMAINKITS_API_KEY.

Risk: Domain availability and pricing can be misleading if suggestions are presented without live verification.

Mitigation: Label domains as available only after DomainKits bulk availability checks and treat prices as current search results.

## Reference(s):

- [DomainKits MCP](https://domainkits.com/mcp)
- [DomainKits Pricing](https://domainkits.com/pricing)
- [ClawHub Skill Page](https://clawhub.ai/abtdomain/skills/domain-generator)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational Markdown with domain candidates, availability layers, pricing notes, and optional MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DomainKits MCP connection; directly registrable domains should only be labeled available after bulk availability verification.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
