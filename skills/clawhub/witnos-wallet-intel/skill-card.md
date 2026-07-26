## Description: <br>
Profile any Base/EVM wallet or x402 buyer before you pay, front, or extend it credit, returning an onchain wallet score, whale detection, address risk, behavioral cluster, and named x402 spend graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andysalvo](https://clawhub.ai/user/andysalvo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External builders, marketplaces, service operators, and agents use this skill to profile unfamiliar Base/EVM wallets before paying, receiving funds, pricing service, or extending credit. It supports counterparty review with wallet intelligence and x402 spend-history context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using paid endpoints can spend USDC through x402. <br>
Mitigation: Keep payment approval under user control and confirm endpoint pricing before each paid request. <br>
Risk: Wallet lookup requests send the queried address to Crest Systems. <br>
Mitigation: Avoid submitting sensitive addresses unless sharing them with the external service is acceptable for the use case. <br>
Risk: Risk labels and wallet scores can be over-relied on for financial decisions. <br>
Mitigation: Treat the results as decision support, not financial advice, and verify independently before transacting. <br>


## Reference(s): <br>
- [Wallet intelligence endpoint](https://data.crestsystems.ai/data/wallet/{address}) <br>
- [Service trust endpoint](https://data.crestsystems.ai/data/service-trust/{address}) <br>
- [x402 market endpoint](https://data.crestsystems.ai/data/x402-market) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Text] <br>
**Output Format:** [Markdown guidance with API endpoint examples and JSON response-field descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve paid x402 requests in USDC to Crest Systems endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
