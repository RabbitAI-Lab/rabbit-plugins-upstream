## Description:

元信MCP yotta-verify-mcp exposes YottaMeta's pre-install static security scanner as a stdio MCP server for scanning agent skills, plugins, and MCP servers before use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to add pre-install trust checks to MCP clients and automated workflows. It provides scan verdicts, audited badges, CI gate checks, and JSON or Markdown reports for targets the user is authorized to evaluate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to edit MCP client configuration and add a persistent cross-session guardrail.

Mitigation: Review and approve any MCP configuration or persistent-memory change before applying it; use manual setup when persistent agent-side changes are not desired.

Risk: Global installation or npx-based use can introduce network and package supply-chain exposure.

Mitigation: Avoid global installation for routine use; prefer local directory or tarball scans when offline or reproducible behavior is required.

Risk: The scanner produces static verdicts that are useful signals but not final security decisions.

Mitigation: Treat the verdict and findings as review inputs and confirm install or block decisions with a human reviewer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [GitHub Repository](https://github.com/YottaMeta/yotta-verify-mcp)
- [yotta-verify CLI](https://github.com/YottaMeta/yotta-verify)
- [Pre-install Trust Checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [MCP JSON responses, Markdown reports, SVG badge files, and inline shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static scan verdicts require human confirmation before install decisions.]

## Skill Version(s):

0.2.4 (source: ClawHub release metadata; artifact frontmatter and package.json report 0.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
