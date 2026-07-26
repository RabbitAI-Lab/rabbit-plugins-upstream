## Description: <br>
Binance Pro helps agents prepare Binance spot and futures account queries, trading commands, leverage changes, stop-loss and take-profit orders, cancellations, and portfolio checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[totaleasy](https://clawhub.ai/user/totaleasy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for Binance balance checks, spot and futures trading command examples, position management, order cancellation, and trade history review. It is intended for users who deliberately want agent assistance with Binance account actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to execute real Binance spot and leveraged futures trades, including orders, cancellations, leverage changes, and position closes. <br>
Mitigation: Use a dedicated Binance API key with withdrawals disabled, minimum permissions, IP restrictions, and small limits; prefer read-only access or Binance testnet unless live trading is explicitly needed. <br>
Risk: Broad always-on routing and trading command examples can lead to unintended account actions if symbols, quantities, leverage, or position direction are wrong. <br>
Mitigation: Require explicit user confirmation before every order, leverage change, cancellation, or position close, and verify the pair, quantity, current position, and stop-loss settings before execution. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/totaleasy/skills/binance-pro) <br>
- [Binance API Documentation](https://binance-docs.github.io/apidocs/) <br>
- [Binance Spot Testnet](https://testnet.binance.vision/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; examples use Binance API credentials and signed REST requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
