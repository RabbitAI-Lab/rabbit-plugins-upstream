## Description:

XCP-ng AIops helps agents operate XCP-ng virtualization fleets through Xen Orchestra, including fleet health, VM, host, pool, storage, snapshot, backup, task, RCA, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect and administer XCP-ng fleets managed by Xen Orchestra, triage common VM, storage, backup, pool, and host issues, and perform guarded VM, snapshot, migration, and storage-rescan actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform disruptive infrastructure changes, including VM power, migration, snapshot, and storage-rescan operations.

Mitigation: Use a dedicated least-privilege Xen Orchestra account, prefer read-only access for triage, require dry-run previews for writes, and reserve write permissions for approved maintenance work.

Risk: The skill relies on stored Xen Orchestra credentials and a master password for non-interactive use.

Mitigation: Avoid plaintext master passwords in shared MCP configuration, protect ~/.xcpng-aiops/ files, and treat audit and encrypted token files as sensitive operational data.

Risk: The release can be installed through mutable package tooling such as uv or uvx.

Mitigation: Pin and verify the package source before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [xcpng-aiops - Capabilities](references/capabilities.md)
- [xcpng-aiops - CLI reference](references/cli-reference.md)
- [xcpng-aiops - Setup & security guide](references/setup-guide.md)
- [Agent guardrails - running xcpng-aiops with a smaller / local model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to invoke CLI or MCP tools that return structured operational data and audit records.]

## Skill Version(s):

0.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
