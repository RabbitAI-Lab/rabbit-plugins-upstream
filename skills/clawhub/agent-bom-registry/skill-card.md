## Description:

MCP server security registry and trust assessment for registry lookups, pre-install marketplace checks, fleet risk scoring, skill file trust assessment, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to assess MCP server trust, review marketplace packages before installation, score server inventories, evaluate skill files, and run optional SAST checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Snyk enrichment for code_scan can involve an external service and an operator-provided SNYK_TOKEN.

Mitigation: Use SNYK_TOKEN only when external enrichment is approved, keep the token in the operator environment, and avoid sending sensitive code or token-bearing output unless policy allows it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text with command examples and structured security findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include registry matches, risk scores, trust findings, and optional SAST results; no telemetry or persistence is disclosed.]

## Skill Version(s):

0.101.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
