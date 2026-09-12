## Description:

truenas-aiops helps agents operate TrueNAS SCALE storage by inspecting system health, diagnosing pool and alert issues, managing pools, datasets, snapshots, disks, services, replication, and cloud-sync tasks, and routing write operations through audit, budget, undo, and risk-tier controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage administrators, and operations agents use this skill to triage and perform governed TrueNAS SCALE storage operations, including health summaries, ZFS pool diagnostics, dataset and snapshot work, service restarts, and replication or cloud-sync inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact TrueNAS write actions, including irreversible snapshot deletion and service restarts.

Mitigation: Use a minimally privileged or read-only TrueNAS API account unless writes are explicitly needed, and require operator review before invoking write tools.

Risk: The release asks users to install executable tooling that handles NAS credentials.

Mitigation: Pin or verify the installed package version before use, run `truenas-aiops doctor`, and keep API keys scoped to the minimum permissions required.

Risk: Credential exposure is possible if users pass real API keys on the command line or place the master password in broad shell or CI environments.

Mitigation: Prefer hidden interactive secret entry, avoid `--value` for real API keys, and restrict `TRUENAS_AIOPS_MASTER_PASSWORD` to the narrowest runtime environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [agent-guardrails.md](references/agent-guardrails.md)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include TrueNAS operation summaries, diagnostic findings, command suggestions, configuration guidance, and audited write-operation guidance.]

## Skill Version(s):

0.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
