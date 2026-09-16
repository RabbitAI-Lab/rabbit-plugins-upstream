## Description:

Fabric AIops helps agents operate controller-managed network fabrics across Cisco Meraki, Cisco Catalyst Center, Arista CloudVision Portal, and UniFi Network, including inventory reads, health analysis, drift detection, and guarded remediation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operations engineers and agent developers use this skill to inspect controller-managed network fabrics, run WAN and fleet-health analyses, identify configuration drift, and execute scoped remediation workflows with audit and undo support where available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs or invokes an external executable that is not pinned by the skill card evidence.

Mitigation: Install only from a trusted package source, prefer a pinned reviewed version, and verify the package before enabling the skill in production.

Risk: The skill can make live controller changes, and the evidence states there is no enforceable read-only mode or approval gate in the skill itself.

Mitigation: Use read-only controller credentials by default, grant write-capable credentials only for planned maintenance, and require operator review before write tools are called.

Risk: Controller credentials and the FABRIC_AIOPS_MASTER_PASSWORD are high-value secrets.

Mitigation: Protect the master password, avoid logging or sharing it, and rotate or revoke controller credentials if exposure is suspected.

Risk: Disabling TLS verification can expose controller sessions to interception outside isolated labs.

Mitigation: Keep verify_ssl enabled for normal use and disable it only in controlled lab environments with self-signed controllers.

Risk: The artifact states the test suite is mock-based and live controller verification has not yet been completed.

Mitigation: Run doctor and start with low-impact read workflows against each target controller before relying on write operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands, configuration snippets, and structured tool-result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include controller-derived operational findings, dry-run previews, audit guidance, and undo-token references.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
