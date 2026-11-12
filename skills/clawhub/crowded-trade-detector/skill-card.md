## Description:

Queries a paid endpoint for data about crowded trades and potential liquidation risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

AI trading agents and developers can query the signal before popular trades to assess crowding as one input to their exposure and risk controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each endpoint call spends USDC, and the listed early-adopter price may change after its stated end date.

Mitigation: Check the current price and endpoint before calling, and fund the wallet only for the intended number of requests.

Risk: The EVM_PRIVATE_KEY environment variable grants signing access to the wallet used for payment.

Mitigation: Use a dedicated, low-balance wallet and keep its private key out of logs, prompts, and shared environments.

Risk: Crowding and contrarian signals can be mistaken for reliable trade instructions or may no longer reflect current conditions.

Mitigation: Check the response timestamp, corroborate the signal, and apply independent exposure and liquidation controls before acting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/crowded-trade-detector)
- [APEX Runner Crowded Trade Detector](https://apexrunner.ai/signals/crowded-trade-detector)
- [APEX Runner Agent Stress Index](https://apexrunner.ai/signals/agent-stress-index)
- [APEX Runner Liquidation Pressure](https://apexrunner.ai/signals/liquidation-pressure)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON response from the x402-authenticated endpoint]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-call payment in USDC on Base; response includes a timestamp.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
