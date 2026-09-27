## Description:

Run local Laya or Von typed classification, scoring, and true-or-false decisions through Decidealot REST or MCP for bounded decisions with probabilities, Docker deployment, model alias inspection, or model memory release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect an agent to a trusted Decidealot endpoint for bounded classification, scoring, and true-or-false decisions. They can also use it to deploy or configure the local REST, MCP, or OpenClaw bridge when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision responses could be treated as authority for irreversible or sensitive actions.

Mitigation: Use decisions as evidence only; keep authorization, ownership checks, final thresholds, and human review for costly mistakes in the caller.

Risk: Requests can send user data to the configured Decidealot endpoint.

Mitigation: Use only a trusted endpoint named by the user, and set DECIDEALOT_API_KEY whenever traffic leaves loopback.

Risk: Long-running deployments that track a mutable image tag can change unexpectedly.

Mitigation: Pin the Decidealot Docker image by version tag or digest for persistent deployments.

## Reference(s):

- [Run and connect to Decidealot](references/setup.md)
- [Decidealot project](https://github.com/psyb0t/decidealot)
- [Decidealot API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Decidealot deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision tasks report typed answers and probabilities; deployment tasks include endpoint health-check confirmation.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
