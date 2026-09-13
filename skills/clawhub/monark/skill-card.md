## Description:

A coverage-controlled gate for agents. You bring your own predictor and nonconformity scores; MONARK calibrates a split-conformal region and returns commit / defer / abstain over YOUR prediction over one public MCP endpoint. Never a probability of being right, never permission to execute a tool. Four tools - attest, gate, cascade, calibrate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kraidle](https://clawhub.ai/user/kraidle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use MONARK to calibrate caller-supplied nonconformity scores and gate their own predictions with commit, defer, or abstain verdicts before a downstream action. The skill is appropriate when the caller controls the predictor, calibration data, score function, and final decision policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Caller-supplied predictions, calibration scores, and related parameters are sent to a public remote endpoint.

Mitigation: Do not send secrets, personal data, or proprietary model outputs unless separately approved for that deployment.

Risk: Returned verdicts may be mistaken for permission to perform consequential actions.

Mitigation: Treat commit, defer, and abstain as advisory coverage verdicts only, and keep authorization decisions in the caller's policy layer.

Risk: Remote endpoint availability is not guaranteed.

Mitigation: Design integrations to tolerate endpoint failure and prefer abstain or local fallback behavior when the service is unavailable.

Risk: Unscoped tool exposure can make more MCP tools available than the integration needs.

Mitigation: Scope exposed tools to the minimum needed set, such as gate and calibrate, where the runtime supports include or exclude controls.

## Reference(s):

- [MONARK ClawHub listing](https://clawhub.ai/kraidle/skills/monark)
- [MONARK MCP endpoint](https://mcp.monarkgate.tech/mcp)
- [MONARK MCP mirror](https://api.monarkgate.tech/mcp)
- [Integration guide](INTEGRATION.md)
- [BYO walkthrough](DEMO.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory integration guidance for a public remote MCP endpoint; verdicts are not authorization for consequential actions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
