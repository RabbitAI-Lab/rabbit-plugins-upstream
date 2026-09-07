## Description:

Author repeated task logic once via ATP (paid per call, no account) and reuse it safely, instead of re-reasoning through the same steps every run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[petroshong](https://clawhub.ai/user/petroshong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external OpenClaw users use this skill to route stable, repeatable task patterns through ATP so later calls can reuse authored logic instead of re-reasoning through the same steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent use a wallet private key to make paid remote calls without built-in per-call spending controls.

Mitigation: Install only with a freshly generated, low-value testnet wallet and add per-call confirmation or a spending cap before routine use.

Risk: Every agent-triggered use can contact the ATP service and send task inputs or descriptions.

Mitigation: Review task inputs before enabling the skill and avoid sending secrets or sensitive data unless the remote service is approved for that use.

## Reference(s):

- [ATP](https://useatp.com)
- [OpenClaw](https://openclaw.ai)
- [OpenClaw creating skills documentation](https://docs.openclaw.ai/tools/creating-skills)
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)
- [ClawHub skill page](https://clawhub.ai/petroshong/skills/atp)
- [Publisher profile](https://clawhub.ai/user/petroshong)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Code]

**Output Format:** [Markdown instructions with inline bash and JSON examples; helper script returns text or JSON from the ATP service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, x402[evm,httpx], and ATP_WALLET_PRIVATE_KEY; calls a paid remote ATP service.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
