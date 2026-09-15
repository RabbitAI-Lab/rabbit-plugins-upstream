## Description:

XYDC MCP (platform.xydc.com) lets an agent use the OOMOL oo CLI to inspect schemas and run XYDC MCP actions for Amazon product, keyword, category, traffic, ranking, advertising, sales, review, and variation insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business analysts use this skill to query XYDC MCP through an OOMOL-connected account, discover live action schemas, and retrieve marketplace intelligence for Amazon products, keywords, categories, traffic, rankings, advertising, sales, reviews, and variations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup path can execute a remote installer script.

Mitigation: Install the oo CLI from a verified, pinned release or trusted package manager instead of blindly piping a remote installer to a shell.

Risk: Some XYDC MCP actions can consume Credits, and timeouts may leave the result or charge status unknown.

Mitigation: Confirm billable actions before execution, reuse returned resource identifiers, and avoid automatic retries after timeouts.

Risk: Generic call_tool requests can be broad enough to hide billable or state-changing behavior.

Mitigation: Inspect the live action schema and behavior annotations before building payloads, and ask for explicit approval before credit-consuming or state-changing calls.

## Reference(s):

- [XYDC MCP homepage](https://platform.xydc.com/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-xydc-mcp)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Markdown]

**Output Format:** [Markdown guidance with oo CLI commands and JSON request/response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return XYDC data with an executionId under meta.executionId; some actions consume Credits or require confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
