## Description:

x402 Compute helps agents manage Singularity Cloud Network compute workflows, including GPU/VPS provisioning, private OpenAI-compatible LLM endpoints, grid inference and node operation, Agent Pods, paid processors, and encrypted Agent Vault backup and migration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to browse, provision, manage, resize, extend, and destroy paid compute, deploy private LLM endpoints or hosted agent pods, run or consume grid inference, publish processors, and manage encrypted agent backups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend wallet funds and create or extend paid compute resources.

Mitigation: Use a dedicated low-balance wallet, review payment details before approval, and avoid non-interactive paid flows unless external approval controls are in place.

Risk: The skill can destroy infrastructure or change persistent hosted agent resources.

Mitigation: Require explicit confirmation for destructive commands, keep API keys revocable, and verify the target instance or pod before acting.

Risk: Private keys, Solana signer keys, compute API keys, pod integration keys, and one-time passwords can grant access to funds or infrastructure.

Mitigation: Keep credentials in explicit environment variables or approved wallet tooling, prefer SSH keys over password fallback, store one-time credentials securely, and revoke keys that are no longer needed.

Risk: Dependencies, runtime package downloads, and curl-piped installers introduce supply-chain risk.

Mitigation: Pin or review dependencies before installation, prefer locally installed wallet binaries, and verify installer source and integrity before running node setup commands.

Risk: Hosted Agent Pods and processors can execute persistent or paid workflows on behalf of a user.

Mitigation: Use capped credentials, review processor pricing and network/payment settings, monitor deployed resources, and disable or destroy resources when the task ends.

## Reference(s):

- [x402 Compute ClawHub Skill Page](https://clawhub.ai/ivaavimusic/skills/x402-compute)
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute)
- [x402 Compute Cloud App](https://cloud.x402compute.cc)
- [x402Compute API Reference](references/api-reference.md)
- [AI Machines](references/ai-machines.md)
- [Agent Pods](references/agent-pods.md)
- [SGL Grid Node Operator](references/node-operator.md)
- [SGL Processors](references/processors.md)
- [Agent Vault](references/agent-vault.md)
- [OpenWallet / OWS](references/openwallet-ows.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python helper script usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to run local Python scripts and call external compute, wallet, payment, and management APIs.]

## Skill Version(s):

1.21.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
