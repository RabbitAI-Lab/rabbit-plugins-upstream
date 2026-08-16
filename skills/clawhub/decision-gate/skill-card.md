## Description:

Decision Gate helps agents commit tamper-evident, hash-chained decision records before high-stakes actions and verify the local JSONL chain afterward.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add a pre-action decision gate for irreversible or high-impact actions such as sending money, releasing data, deploying configuration, or signing transactions. It records local decision claims before execution so later reviewers can check ordering and tamper evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local decision log may contain action IDs, decision labels, risk bands, evidence tags, source references, and outcome references.

Mitigation: Do not store secrets or raw sensitive data in log fields; use opaque identifiers and bounded tags.

Risk: By default the skill writes a persistent JSONL log in the working directory.

Mitigation: Set DECISION_GATE_LOG_PATH deliberately for environments where the working directory is not an appropriate storage location.

Risk: A local hash-chained log shows ordering and tamper evidence, but it does not independently prove that logged evidence classes reflect what the agent actually evaluated.

Mitigation: Use externally owned validation or a separate verifier for high-impact actions where self-authored records are not sufficient.

## Reference(s):

- [Decision Gate product page](https://soulscore.xyz/decision-gate?src=clawhub)
- [Zero Trust for AI Agents analysis](https://mnemehq.com/insights/zero-trust-for-ai-agents-architectural-governance/)
- [soulscore methodology](https://soulscore.xyz/methodology?src=clawhub)
- [ClawHub skill page](https://clawhub.ai/vaahl-dev/skills/decision-gate)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Guidance]

**Output Format:** [Python API usage, shell commands, JSONL log records, and text verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a persistent local decision log at DECISION_GATE_LOG_PATH or ./decision_gate.log.jsonl by default.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
