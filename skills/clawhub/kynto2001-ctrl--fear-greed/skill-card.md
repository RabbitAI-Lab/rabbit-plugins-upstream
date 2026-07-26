## Description: <br>
Composite Fear & Greed index with source and staleness metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and trading agents use this skill to retrieve a paid real-time Fear & Greed market signal with source and staleness metadata before DCA entries, position sizing, or market-risk checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an EVM private key and may spend wallet funds for paid x402 requests. <br>
Mitigation: Use a dedicated wallet with limited USDC on Base and monitor repeated calls. <br>
Risk: Exposure of EVM_PRIVATE_KEY could compromise the funded wallet. <br>
Mitigation: Keep EVM_PRIVATE_KEY secret and scope it to a low-balance wallet used only for this skill. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/kynto2001-ctrl/skills/fear-greed) <br>
- [APEX Runner Fear Greed signal](https://apexrunner.ai/signals/fear-greed) <br>
- [APEX Runner pricing tier check](https://apexrunner.ai/signals/my-pricing) <br>
- [Related signal: fg-micro](https://apexrunner.ai/signals/fg-micro) <br>
- [Related signal: dca-signal](https://apexrunner.ai/signals/dca-signal) <br>
- [Related signal: dca-reentry-gate](https://apexrunner.ai/signals/dca-reentry-gate) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON response from an x402-authenticated GET request, with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EVM_PRIVATE_KEY for a wallet funded with USDC on Base; each invocation may incur a small paid request charge.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
