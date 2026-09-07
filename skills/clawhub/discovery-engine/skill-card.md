## Description:

Discovery helps agents find statistically validated patterns, feature interactions, subgroup effects, citations, and novelty signals in tabular datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and data science agents use this skill to upload tabular datasets to Disco, choose a target column and exclusions, run public or private analyses, and return statistically validated findings. It is intended for exploratory pattern discovery rather than summary statistics, visualization, filtering, SQL querying, or standalone literature search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can upload datasets to Disco, and public analyses publish results to the public gallery.

Mitigation: Use private mode for confidential data, confirm visibility before analysis, and avoid sensitive or regulated datasets unless the provider's data handling is understood.

Risk: The skill exposes billing, subscription, payment-method, and credit-purchase capabilities.

Mitigation: Require explicit human approval before attaching payment methods, purchasing credits, or changing subscriptions.

Risk: Including identifiers, leakage columns, tautological columns, or derived target fields can produce findings that are statistically real but not meaningful discoveries.

Mitigation: Review columns before running analysis and exclude identifiers, leakage, tautological fields, and derived target components.

Risk: API keys and account operations can grant access to datasets, credits, and reports.

Mitigation: Keep DISCOVERY_API_KEY secret, do not expose it in prompts or logs, and use account checks before paid private analyses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco homepage](https://disco.leap-labs.com)
- [Disco MCP server](https://disco.leap-labs.com/mcp)
- [Disco API keys](https://disco.leap-labs.com/developers)
- [Disco Python SDK](docs/python-sdk.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON/API results and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured pattern results, p-values, effect sizes, citations, novelty classifications, report links, and account or billing guidance.]

## Skill Version(s):

0.2.173 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
