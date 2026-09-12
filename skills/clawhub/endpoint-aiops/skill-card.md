## Description:

Endpoint AIops helps agents inspect and operate managed-endpoint fleets, including fleet health, inventory, login-storm analysis, patch and configuration drift, health scoring, profile assignment, and endpoint reboots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and endpoint operations teams use this skill to triage managed-endpoint fleets, rank unhealthy endpoints, investigate login storms, detect patch or configuration drift, and perform guarded remediation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP write tools can reboot endpoints or change profiles without an enforced skill-side read-only mode or approval gate.

Mitigation: Use a read-only management account by default, expose write tools only where operators can approve changes out of band, and require dry-run review before state-changing actions.

Risk: Broad administrator credentials in shared environments could allow unintended fleet changes.

Mitigation: Avoid exporting broad administrator passwords into shared shells, keep credentials scoped to the minimum needed role, and unlock the encrypted store only for trusted sessions.

Risk: Endpoint-management REST paths and dialects are documented as not yet exercised against a live management server.

Mitigation: Run endpoint-aiops doctor, validate against a non-production target first, and compare tool output with the management console before relying on remediation workflows.

Risk: Disabling TLS verification for self-signed lab certificates can weaken connection security.

Mitigation: Keep TLS verification enabled for normal deployments and disable it only for controlled lab certificates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/endpoint-aiops)
- [Endpoint-AIops Repository](https://github.com/AIops-tools/Endpoint-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs may include capped lists with returned, limit, and truncated fields; write actions are audited and may support dry-run or undo metadata.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
