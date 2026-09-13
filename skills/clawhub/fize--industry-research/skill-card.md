## Description:

Provides a standard operating procedure for deep industry and supply-chain research, including value-chain mapping, cycle and inflection-point analysis, competitive landscape review, policy and regulatory assessment, and public-market asset mapping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to structure fact-checked industry research reports for sectors, value chains, competitive landscapes, and market-traded assets. It is intended as a research and reporting aid rather than financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industry reports may be mistaken for financial advice.

Mitigation: Present outputs as research support only and require users to verify investment decisions with qualified financial professionals and authoritative market data.

Risk: The skill may invoke external research tools and market-data workflows.

Mitigation: Review tool permissions, data-source access, and organization policy before enabling the skill in an agent environment.

Risk: Users who do not want Chinese output or broad industry-analysis activation may encounter mismatched locale or trigger behavior.

Mitigation: Set clear language preferences and activation boundaries before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/industry-research)
- [Industry Research skill source](artifact/SKILL.md)
- [market/SKILL.md](../market/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown industry research report with sourced evidence markers and comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires verifiable market, policy, PDF, and financial data; instructs fail-fast behavior when core figures cannot be sourced.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
