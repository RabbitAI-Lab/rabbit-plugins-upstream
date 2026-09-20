## Description:

Inspects and manages VMware NSX networking through NSX Manager for segments, gateways, NAT, routing, IP pools, health checks, and connectivity troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect NSX inventory and health, troubleshoot VM connectivity, and perform explicitly requested NSX networking changes with audit and approval controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform state-changing NSX networking operations, including segment, gateway, NAT, route, IP pool, and Tier-0 BGP changes.

Mitigation: Use least-privilege NSX accounts, require explicit user approval for writes, and apply policy deny rules for production targets where agents should not make changes.

Risk: MCP non-delete write tools execute real changes once called, even though delete tools preview by default.

Mitigation: Use workflows that respect explicit approval boundaries, review delete previews before confirm=True, and prefer dry-run or read-only diagnosis before changes.

Risk: NSX credentials are sensitive, and a local .env file may expose passwords if filesystem access is not controlled.

Mitigation: Protect the .env file, prefer secret-manager injection for production, and avoid storing plaintext credentials where possible.

Risk: Disabling TLS verification can expose NSX Manager connections outside isolated labs.

Mitigation: Keep TLS verification enabled for real environments and use a private CA bundle through SSL_CERT_FILE or SSL_CERT_DIR when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage](https://github.com/vmware-skills/VMware-NSX)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool guidance and NSX operation summaries; write actions require explicit user intent and are audit-logged.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
