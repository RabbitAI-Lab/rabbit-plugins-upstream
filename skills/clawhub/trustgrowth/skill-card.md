## Description:

TrustGrowth connects agents to TrustGrowth API and MCP capabilities and persisted growth evidence for normalized SEO history, prioritization, workflows, and verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and SEO operators use this skill to connect an agent to an existing TrustGrowth account, inspect available MCP or REST capabilities, and retrieve persisted growth evidence for reports or workflow routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a TrustGrowth API key and can access SEO workflow data.

Mitigation: Confirm the user intends to connect TrustGrowth, keep the API key scoped to the intended access, and never print the key.

Risk: Some available actions can write data, consume credits, or affect outward-facing workflows.

Mitigation: Require owner approval before credit-consuming, irreversible, or outward-facing actions such as audits, strategy regeneration, and link review updates.

Risk: Using endpoints or fields outside the published contract can produce unreliable behavior.

Mitigation: Use only endpoints listed in the contract or live capability manifest, honor rate-limit headers, and report authorization or plan errors verbatim.

Risk: SEO reports can become misleading if missing or unverified measurements are treated as facts.

Mitigation: Keep null values as null, label unavailable evidence as unknown, and require validated evidence before drawing conclusions.

## Reference(s):

- [TrustGrowth Developer Docs](https://trustgrowth.ai/developers)
- [TrustGrowth Contract](references/contract.md)
- [Connectors and Categories](references/connectors.md)
- [Reporting Contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API or MCP call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated TrustGrowth REST or MCP calls; API key values must not be printed.]

## Skill Version(s):

1.0.1 (source: evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
