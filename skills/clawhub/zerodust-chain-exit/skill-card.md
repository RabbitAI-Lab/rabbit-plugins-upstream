## Description: <br>
Sweep 100% of native gas tokens from EIP-7702 compatible chains, leaving exactly zero balance across supported mainnet chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zerodustxyz](https://clawhub.ai/user/zerodustxyz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to help users fully exit or consolidate native gas-token balances from supported EIP-7702 chains. It guides quote retrieval, authorization, signing, sweep submission, and status polling for single-chain or batch sweeps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides full-balance crypto sweeps, which can move all native tokens from a source chain. <br>
Mitigation: Before signing, verify the ZeroDust provider, source chain, destination chain and address, exact amount, fees, EIP-7702 delegation details, and revocation status. <br>
Risk: Batch sweeps can apply the same high-impact action across multiple chains. <br>
Mitigation: Review each chain individually and avoid batch execution unless every source chain, destination, fee, and amount has been confirmed. <br>


## Reference(s): <br>
- [ZeroDust Skill Page](https://clawhub.ai/zerodustxyz/skills/zerodust-chain-exit) <br>
- [ZeroDust API Documentation](https://zerodust-backend-production.up.railway.app/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with curl commands and JSON request/response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZERODUST_API_KEY and user wallet signatures for EIP-7702 delegation, revocation, and sweep authorization.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
