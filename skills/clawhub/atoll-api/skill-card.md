## Description:

Use Atoll for project, issue, goal, KPI, initiative, milestone, comment, dependency, and workflow operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operational agents use this skill to manage Atoll project work through MCP, CLI, or API while preserving strategy-to-execution relationships. It guides profile selection, read-before-write sequencing, safe state changes, and readback verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide credentialed Atoll actions across project-management resources.

Mitigation: Use narrowly scoped Atoll agent profiles and verify authorization scope before state-changing operations.

Risk: Secrets or API keys could be exposed if users paste them into chat or shell history.

Mitigation: Store credentials in appropriate configuration or environment variables and rotate any secret that was shared in chat.

Risk: Billing, key management, hard deletes, webhook changes, and inbox handling can have high operational impact.

Mitigation: Require explicit human intent before these operations and perform readback verification after any accepted change.

Risk: Referenced npm packages may change after release.

Mitigation: Pin or verify npm package versions before installation in sensitive environments.

## Reference(s):

- [Atoll](https://atollhq.com)
- [Atoll ClawHub Skill](https://clawhub.ai/doubledipcode/skills/atoll-api)
- [Atoll API Endpoint Reference](references/api-endpoints.md)
- [Atoll API Field Reference](references/api-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and API references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use live Atoll tool, CLI, or API responses for project-specific facts and verify state-changing results with readback.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
