## Description:

Accurately and efficiently extracts and analyzes pharmaceutical company intelligence to provide professional company profiles and investment or collaboration recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, life-science analysts, and business development teams use this skill to profile pharmaceutical companies, including company overview, financing history, pipeline, drug transactions, and patent layout. It relies on user-configured PatSnap LifeScience MCP services and returns evidence-oriented research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries sent through the configured PatSnap MCP service may include sensitive company, drug, patent, or research interests.

Mitigation: Confirm the user trusts PatSnap for those queries before installation or use, and keep the PatSnap API key private.

Risk: Investment or collaboration recommendations may be incomplete, stale, or unsuitable as the sole basis for business decisions.

Mitigation: Treat generated recommendations as research support and review them against authoritative sources and internal decision processes.

Risk: The skill depends on a configured PatSnap LifeScience MCP service; missing or invalid connectivity can prevent useful output.

Mitigation: Verify the MCP service connection and authentication before processing user research requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/company-profiling)
- [PatSnap Pharma Intelligence MCP server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [PatSnap Dev Portal](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown report with structured sections, citations, tables where useful, and inline shell commands for setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are expected to include an Abstract, Roman-numeral sections, a Conclusion, generation dates, data sources, and a disclaimer.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact metadata reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
