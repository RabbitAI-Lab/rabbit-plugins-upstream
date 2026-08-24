## Description:

Pangolinfo Amazon Niche Finder helps agents browse and search Amazon category trees, resolve category paths, and filter categories or niches by commercial metrics such as sales, search volume, returns, growth, and competition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through Amazon category and niche research with Pangolinfo MCP tools. It supports category tree browsing, category search, category path resolution, metric-based category filtering, and low-competition niche screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill instructs the agent to access and reason about a raw Pangolinfo API key from the environment.

Mitigation: Prefer storing credentials in the MCP server or a managed secret store, and avoid asking the agent to print, validate, transform, or troubleshoot the raw key value.

Risk: Some Pangolinfo category and niche operations consume paid credits, with niche filtering identified in the artifact as the most expensive path.

Mitigation: Confirm the user's budget before expensive niche filtering and keep default runs within the skill's Fast posture unless the user asks for a deeper run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-niche)
- [Pangolinfo website](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown]

**Output Format:** [Markdown reports with structured tables, concise recommendations, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Pangolinfo MCP tool results as the source for reported category and niche metrics; normal presentation avoids raw JSON.]

## Skill Version(s):

4.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
