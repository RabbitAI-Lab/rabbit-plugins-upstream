## Description:

Enables governed Nutanix Prism Central v4 operations for estate health, cluster and host inventory, VM lifecycle, storage, networking, data protection, alerts, LCM, capacity forecasting, and RCA workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect, diagnose, and operate Nutanix Prism Central v4 estates through an agent, including VM lifecycle actions, storage and DR workflows, alert RCA, LCM upgrades, and capacity runway checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent destructive write access to Nutanix infrastructure without an enforced approval or read-only gate.

Mitigation: Use a dedicated least-privilege Prism Central account, begin with read-only permissions where possible, require human approval for write workflows, and use dry-run previews before destructive operations.

Risk: A broad agent session with privileged credentials could perform unintended infrastructure changes.

Mitigation: Avoid privileged write credentials in broad sessions, scope credentials to the task, protect the master password from shell history and CI logs, and review audit output after operations.

Risk: The skill installs an external package that the security evidence describes as unpinned.

Mitigation: Pin or verify the nutanix-aiops package before deployment and install only from sources trusted by the operating team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/nutanix-aiops)
- [Project homepage](https://github.com/AIops-tools/Nutanix-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured infrastructure operation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Prism Central operation plans, diagnostics, dry-run previews, and safety guidance.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
