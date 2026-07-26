## Description: <br>
Fetch a pre-transaction risk score and advisory recommendation for tokens on Solana, Base, Ethereum, Arbitrum, BSC, and HyperEVM before the user trades, swaps, or provides liquidity. Read-only; never signs or moves funds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[babyscaphe](https://clawhub.ai/user/babyscaphe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Bitfence before token swaps, DEX trades, liquidity provision, or staking involving unfamiliar tokens. It returns advisory risk scoring and recommendations so the user can decide whether to proceed, seek approval, or stop. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid risk checks may spend USDC on Base mainnet. <br>
Mitigation: Inform the user about x402 payment before the first paid check in a session and avoid loops, polling, or batch calls. <br>
Risk: Contextual checks may share position size and total portfolio size with Bitfence. <br>
Mitigation: Use contextual analysis only after the user opts in to sharing those values. <br>
Risk: A risk score is advisory and cannot guarantee token safety. <br>
Mitigation: Present recommendations, confidence, flags, and reasoning clearly while leaving the final decision to the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/babyscaphe/skills/bitfence) <br>
- [Bitfence website](https://www.bitfence.ai) <br>
- [Bitfence API root](https://api.bitfence.ai) <br>
- [Bitfence X profile](https://x.com/bitfenceai) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Guidance, JSON] <br>
**Output Format:** [JSON risk report with concise human-facing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only advisory output; contextual checks may include position-aware risk fields when the user opts in.] <br>

## Skill Version(s): <br>
0.7.7 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
