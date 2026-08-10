## Description:

Orchestrates a Planner, Coder, Checker, and Memowriter loop for contract-driven coding tasks with staged gates, competitive implementations, scoring, documentation, and workboard traceability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wljmmx](https://clawhub.ai/user/wljmmx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route medium and high complexity coding work through a staged multi-agent workflow: contract negotiation, implementation, review, quality-gate decisions, and documentation. It is intended for OpenClaw environments that have the named agents, workboard tooling, QQ sessions, and model endpoints configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create persistent workboard tasks and message fixed agent sessions without an explicit user confirmation step.

Mitigation: Install only in an intended OpenClaw orchestration environment and add a confirmation step before dispatching agents or creating persistent workboard tasks.

Risk: Long-running coding and review work may continue through configured agents and workboard state after the initial request.

Mitigation: Monitor workboard status, require heartbeat updates for long tasks, and pause for human review on blocked decisions, repeated failures, or high-complexity review gates.

## Reference(s):

- [Competitive Agent Loop on ClawHub](https://clawhub.ai/wljmmx/skills/competitive-agent-loop)
- [Sprint Contract Template](artifact/templates/sprint-contract.yaml)
- [REST API Example](artifact/examples/rest-api-example.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, json, guidance]

**Output Format:** [Markdown instructions with code blocks, JSON scoring records, workboard updates, and file paths for generated artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent workboard tasks and comments, dispatch configured agent sessions, and produce repository files such as code, tests, review reports, sprint contracts, and documentation.]

## Skill Version(s):

2.0.1 (source: server release evidence and artifact heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
