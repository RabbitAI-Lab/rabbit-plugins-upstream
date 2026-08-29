## Description:

This skill helps agent architects, platform engineers, and enterprise development teams plan AI-HIVE Agent Harness workflows with layered architecture, tool contracts, state models, evaluation gates, and operating runbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn Agent Harness requirements into an auditable plan for model routing, tool boundaries, state handling, permissions, cost controls, and acceptance checks. It is aimed at AI-HIVE content-agent delivery where teams need reusable architecture and review evidence rather than prompt-only advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI_HIVE_API_KEY could be exposed if placed in files, logs, screenshots, or shared plan records.

Mitigation: Keep the key only in a secure environment variable or credential store and review generated files before sharing.

Risk: Paid, batch, external publishing, deletion, or permission-changing actions could create cost or operational impact.

Mitigation: Require explicit user confirmation before any paid, batch, external publishing, deletion, or permission-changing action.

Risk: Model availability, parameters, and pricing can become stale.

Mitigation: Query current AI-HIVE model availability and pricing snapshots at runtime, then record the selected model, route, price snapshot, task ID, status, and outputs.

Risk: Generated harness plans may contain incorrect facts, unauthorized material assumptions, or unvalidated architecture choices.

Mitigation: Review plan files before execution or sharing, verify facts and material rights, and accept changes through documented evaluation gates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-hot-agent-harness-engineering)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [Harness Agents documentation](https://developer.harness.io/3k-docs/ai/harness-agents/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash examples and JSON plan records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local execution plan records; live model queries require AI_HIVE_API_KEY in a secure environment variable.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
