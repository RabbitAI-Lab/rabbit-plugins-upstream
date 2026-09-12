## Description:

vmware-pilot helps agents design, review, execute, and manage multi-step VMware workflows with approval gates, persisted state, audit logging, and explicit best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware platform engineers and operations teams use this skill to coordinate multi-step VMware workflows across companion skills, especially when tasks require checkpoints, human approval, rollback planning, incident response, maintenance, or compliance scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow steps can lead to real VMware production changes when dispatched through companion skills.

Mitigation: Review every generated workflow before execution, run structural review where available, and keep destructive or unclassifiable steps behind explicit approval gates.

Risk: Rollback is explicit and best-effort, and some dispatched steps may not be visible to pilot's own rollback state.

Mitigation: Ask before undoing failed workflows and use each completed step's rollback tool and rollback parameters in reverse order when manual rollback is required.

Risk: Credential-returning companion steps can expose live VMware or Kubernetes access material.

Mitigation: Run credential-returning steps only after approval, write credentials to owner-only files, and avoid printing tokens into chat or logs.

Risk: Local workflow, audit, baseline, and template files can contain sensitive infrastructure data.

Mitigation: Protect files under ~/.vmware with owner-only permissions and follow the skill guidance for audit and baseline storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Project homepage](https://github.com/vmware-skills/VMware-Pilot)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Workflow Design Guide](references/workflow-design.md)
- [Integration Patterns](references/integration-patterns.md)
- [Built-in Templates](references/templates.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with workflow steps, MCP tool calls, shell commands, and YAML or JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plans and operational guidance for the calling agent; infrastructure-changing steps are dispatched through companion VMware skills.]

## Skill Version(s):

1.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
