## Description: <br>
MinIO AIops helps agents diagnose and operate MinIO object storage with governed health, capacity, exposure, lifecycle, healing, and bucket-management tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, storage operators, and site reliability engineers use this skill to inspect MinIO health, capacity pressure, bucket exposure, lifecycle gaps, healing status, and selected governed bucket changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes storage-changing MinIO operations without a built-in read-only mode or approval gate. <br>
Mitigation: Use a read-only MinIO IAM policy for observe-only sessions, require operator approval for writes, and prefer dry-run previews before applying changes. <br>
Risk: Operational access keys can affect real MinIO buckets, policies, lifecycle rules, quotas, and incomplete uploads. <br>
Mitigation: Grant the least-privileged key needed for the task and review the local audit and undo logs after write sessions. <br>
Risk: Transport or secret handling mistakes can expose credentials or weaken connection security. <br>
Mitigation: Keep TLS verification enabled outside labs, store secrets in the encrypted secret store, and avoid legacy plaintext environment secrets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/minio-aiops) <br>
- [Project Homepage](https://github.com/AIops-tools/MinIO-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bounded listings with returned, limit, and truncated indicators; write actions should be handled as dry-run previews or governed tool calls when appropriate.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
