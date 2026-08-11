## Description:

Decision Gate helps agents commit a local, hash-chained decision record before high-stakes actions so later reviewers can detect edits, insertions, or reordering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create tamper-evident pre-action records for irreversible or high-impact actions such as transfers, data releases, deployments, or signed transactions. It is intended to make self-authored decision logs harder to backfill while preserving a local, dependency-free workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision records can expose sensitive context if action IDs, evidence fields, source references, or outcome references contain secrets or raw personal data.

Mitigation: Use opaque action IDs, log evidence classes rather than raw evidence, and keep PII and secrets out of the configured JSONL log.

Risk: A local hash chain can detect later tampering but cannot independently prove that the recorded evidence was complete or that the caller did not write a favorable record immediately before acting.

Mitigation: Use the local log as a pre-action commitment layer, and route high-risk or irreversible actions to an independent verifier when external assurance is required.

Risk: The default log path may place decision records in an unintended working directory.

Mitigation: Set DECISION_GATE_LOG_PATH deliberately and apply appropriate filesystem access controls and retention practices.

## Reference(s):

- [Decision Gate ClawHub Release](https://clawhub.ai/vaahl-dev/skills/decision-gate)
- [Decision Gate Product Page](https://soulscore.xyz/decision-gate)
- [Soulscore Methodology](https://soulscore.xyz/methodology)
- [Zero Trust for AI Agents Analysis](https://mnemehq.com/insights/zero-trust-for-ai-agents-architectural-governance/)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with Python examples and local JSONL log output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local append-only JSONL decision and outcome records; DECISION_GATE_LOG_PATH can configure the log path.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
