## Description:

Prove Before Act accountability integration for AI agents. REST API, MCP, and x402. The @jasonxkensei/xproof ClawHub slug is a legacy compatibility identifier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jasonxkensei](https://clawhub.ai/user/jasonxkensei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add proof anchoring, proof verification, MCP integration, and x402 payment guidance to AI agent workflows. It helps agents hash content locally, submit selected proof metadata to Prove Before Act, and verify returned proof records before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proof hashes and selected metadata may be anchored with a third-party service and remain publicly visible.

Mitigation: Use placeholder or non-sensitive filenames and author names, and confirm that permanent public anchoring is acceptable before certification.

Risk: Raw files, prompts, secrets, or other sensitive content could be exposed if an agent sends content instead of hashes.

Mitigation: Hash content locally and send only the SHA-256 digest and intentionally selected metadata.

Risk: The pm_ API key can authorize service use if leaked.

Mitigation: Treat the API key as a secret, avoid logging it, and keep it out of repositories and shared transcripts.

Risk: x402 mode can let an autonomous agent initiate USDC payments.

Mitigation: Enable x402 only with explicit spending limits and approval rules.

## Reference(s):

- [Prove Before Act homepage](https://provebeforeact.com)
- [Prove Before Act agent context](https://provebeforeact.com/agent-context)
- [ClawHub skill page](https://clawhub.ai/jasonxkensei/skills/xproof)
- [API Reference](references/api-reference.md)
- [Certification API](references/certification.md)
- [MCP Server](references/mcp.md)
- [x402 Payments](references/x402.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for external proof anchoring; agents must hash content locally and configure API-key or x402 payment use before calling services.]

## Skill Version(s):

4.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
