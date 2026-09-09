## Description:

Static security checkup for MCP / AI-agent server configs — 14 automated checks covering hardcoded cloud credentials, arbitrary shell/command execution, writable filesystem mounts, missing egress allowlists (SSRF surface), plaintext HTTP endpoints, unpinned npx/uvx remote launchers, and over-broad tool clustering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dshcorrectover](https://clawhub.ai/user/dshcorrectover)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to scan MCP or AI-agent server configuration JSON before connecting it to an agent, producing a local first-pass risk report with remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional online mode can upload sensitive MCP configuration content and local CCS or payment credentials to a configured endpoint.

Mitigation: Use local mode for configurations containing secrets; use --online only after reviewing the destination, clearing CCS_API_ENDPOINT unless intentionally set, and avoiding CCS_API_TOKEN or payment proof values for noncanonical endpoints.

Risk: The static checks are a first-pass screening layer and do not evaluate live endpoint behavior, tool implementation code, permission boundaries, or data flows.

Mitigation: Treat findings as triage output and require qualified manual review before making security or compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dshcorrectover/skills/mcp-config-security-checkup)
- [Correctover homepage](https://correctover.com/?utm_source=clawhub&utm_medium=skill&utm_campaign=ccs_checkup)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Console text report or machine-readable JSON with risk level, counts, rule IDs, server names, redacted evidence, and remediation advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local mode is default; optional online mode may submit the checked configuration to a Correctover hosted service.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
