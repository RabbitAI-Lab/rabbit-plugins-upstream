## Description:

Decision Gate helps agents commit a tamper-evident, hash-chained decision record before high-stakes actions, with optional third-party verification for claims that need independent receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent is about to perform an irreversible or high-impact action and needs a pre-action decision record. It supports local hash-chain verification and can pair with an external verifier for independent receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes persistent local decision records, so records may be stored somewhere unexpected if the log path is not reviewed.

Mitigation: Set and review DECISION_GATE_LOG_PATH before use so the append-only manifest is stored in an approved location.

Risk: Broad audit and accountability trigger phrases may cause the skill to activate for more situations than exact-name invocation.

Mitigation: Review agent trigger policy and invoke the skill deliberately for irreversible, high-impact, or compliance-sensitive actions.

Risk: A local self-authored log can show ordering and tamper evidence, but it cannot by itself prove the logged evidence classes were correct.

Mitigation: Use the external decision-gate-verifier pattern for high-risk claims that require independent verification.

Risk: Decision records may become less useful if evidence sources are stale or not bound to a version.

Mitigation: Populate source_refs with source snapshots or versions for regulatory, time-sensitive, or otherwise freshness-dependent inputs.

## Reference(s):

- [Decision Gate ClawHub page](https://clawhub.ai/vaahl-dev/skills/decision-gate)
- [Decision Gate homepage](https://soulscore.xyz/decision-gate)
- [Zero Trust for AI Agents analysis](https://mnemehq.com/insights/zero-trust-for-ai-agents-architectural-governance/)
- [Soulscore methodology](https://soulscore.xyz/methodology)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local JSONL decision and outcome records when its Python helper is used.]

## Skill Version(s):

1.3.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
