## Description:

Get Chinese financial data via AKShare, including stock, fund, bond, futures, macroeconomic, and related market data.

This skill is for research and development only.

## Publisher:

[anyjohn](https://clawhub.ai/user/anyjohn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance analysts use this skill to guide an agent in retrieving public Chinese and related market data through AKShare APIs. It is suited for research and data exploration workflows that need code examples, API names, and troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad finance trigger terms may activate this skill for general finance questions where AKShare is not the intended source.

Mitigation: Confirm AKShare is the intended data source before relying on results or installing packages.

Risk: Public market data can be delayed, stale, unavailable, or inconsistent across sources.

Mitigation: Validate time ranges, check update notes, and compare important results against multiple sources before using them for decisions.

Risk: Financial data may be mistaken for investment advice.

Mitigation: Treat outputs as research data and require human review before any financial decision.

## Reference(s):

- [AKShare Complete API List](references/api-list.md)
- [AKShare Documentation](https://akshare.akfamily.xyz/)
- [AKShare GitHub](https://github.com/akfamily/akshare)
- [AKShare Installation Guide](https://akshare.akfamily.xyz/installation.html)
- [AKShare Interface List](https://akshare.akfamily.xyz/tutorial.html)
- [AKShare Interface Changelog](https://akshare.akfamily.xyz/changelog.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes AKShare API names, installation commands, usage examples, and data-quality cautions.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
