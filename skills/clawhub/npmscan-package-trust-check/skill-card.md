## Description:

Investigate whether one specific npm package is trustworthy — maintainer/ownership takeover signals, publish-provenance mismatches, and risky install scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salemalem](https://clawhub.ai/user/salemalem)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to investigate trust signals for one named npm package and, optionally, a specific version, including vulnerabilities, maintainer history, publish provenance, and install scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The investigation depends on data returned by the external NPMScan service, and a clean report cannot guarantee package safety.

Mitigation: Connect only if you trust NPMScan, and independently verify important findings before relying on them.

## Reference(s):

- [NPMScan MCP service](https://npmscan.com/api/mcp)
- [ClawHub skill release](https://clawhub.ai/salemalem/skills/npmscan-package-trust-check)
- [Test prompts](references/test-prompts.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown findings report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single-package report that states findings by check and links to the NPMScan write-up.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
