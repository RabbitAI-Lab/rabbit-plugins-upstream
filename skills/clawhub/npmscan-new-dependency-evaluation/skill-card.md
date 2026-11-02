## Description:

Helps developers choose a new npm dependency by comparing named candidates or shortlisting options from a described need before installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salemalem](https://clawhub.ai/user/salemalem)

### License/Terms of Use:

MIT-0

## Use Case:

Developers deciding which npm dependency to add use this skill to compare two to five named options or shortlist candidates for a stated need, before installing anything.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package names and search descriptions are sent to the external NPMScan service and could reveal confidential project details.

Mitigation: Use generic queries and omit confidential project details.

Risk: Comparison recommendations may not capture every package concern and could be mistaken for approval to install.

Mitigation: Treat recommendations as comparison advice and review packages separately before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/salemalem/skills/npmscan-new-dependency-evaluation)
- [NPMScan MCP service](https://npmscan.com/api/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown package comparisons and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes package comparison details, a recommended pick, and rationale.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
