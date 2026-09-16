## Description:

Operates XCP-ng virtualization fleets through Xen Orchestra with health overviews, RCA workflows, inventory reads, and governed VM, storage, snapshot, and migration writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect, triage, and administer XCP-ng fleets managed by Xen Orchestra. It is suited for fleet health checks, VM and storage RCA, backup failure analysis, snapshot workflows, and controlled operational writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact infrastructure writes through Xen Orchestra, including VM power operations, migration, SR rescan, and snapshot changes.

Mitigation: Use a dedicated least-privilege Xen Orchestra account and prefer read-only ACLs for triage sessions so unauthorized writes fail at Xen Orchestra.

Risk: Snapshot delete and snapshot revert are irreversible operations.

Mitigation: Avoid unattended use of irreversible snapshot actions; require dry-run review, operator confirmation, and a current snapshot before rollback workflows.

Risk: The MCP configuration may expose the master password if stored in a broadly readable file.

Mitigation: Restrict permissions on MCP configuration and secret material, and avoid storing the master password where other users or tools can read it.

Risk: The runtime package is fetched externally and may be unpinned unless the operator controls the installed version.

Mitigation: Pin or verify the exact xcpng-aiops package version before use.

Risk: Stopping the VM that runs Xen Orchestra can remove the API path needed for recovery if the self-VM UUID is not declared.

Mitigation: Configure the Xen Orchestra self-VM UUID where available and keep an agent prompt rule to avoid stopping Xen Orchestra itself.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [xcpng-aiops - Capabilities](references/capabilities.md)
- [xcpng-aiops - CLI reference](references/cli-reference.md)
- [xcpng-aiops - Setup & security guide](references/setup-guide.md)
- [Agent guardrails - running xcpng-aiops with a smaller / local model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-shaped tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can invoke CLI or MCP workflows that return fleet summaries, listings, RCA findings, dry-run previews, audit references, and undo identifiers.]

## Skill Version(s):

0.8.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
