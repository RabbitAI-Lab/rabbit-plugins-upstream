## Description:

Helps network operators inspect, diagnose, back up, and change supported network devices through CLI and MCP tools, with optional NetBox lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and engineers use this skill to inspect and troubleshoot Cisco, Arista, and Juniper devices, compare and back up configurations, and perform controlled configuration changes. Optional NetBox lookups provide source-of-truth context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuration write tools can disrupt network access, and the skill has no read-only mode or mandatory approval gate.

Mitigation: Use read-only device and NetBox credentials by default; allow write-capable credentials only in controlled change windows and require human review of diffs before MCP writes.

Risk: Legacy plaintext environment fallbacks can expose device passwords or the NetBox token.

Mitigation: Use the encrypted credential store instead of legacy .env or plaintext environment fallbacks.

Risk: Some device drivers cannot provide an automatic revert timer for configuration commits.

Mitigation: Check commit safety warnings, verify device reachability before confirmation, and maintain a tested backup and rollback plan.

Risk: Fetching an unpinned CLI fallback may introduce unexpected software changes.

Mitigation: Prefer the installed, pinned entry point over the uvx fallback.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/network-aiops)
- [Project homepage (listed in release metadata)](https://github.com/AIops-tools/Network-AIops)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown guidance and command examples; structured tool responses when using MCP]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device-health findings, configuration diffs, and backup guidance; review changes before execution.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
