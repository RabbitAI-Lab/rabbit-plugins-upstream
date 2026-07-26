## Description: <br>
Scans live stablecoin yield pools across major DeFi protocols and chains using the DeFiLlama pools API, with filters for TVL, APY range, chain, and reward-emission composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External DeFi users, treasury operators, and developers use this skill to shortlist stablecoin yield opportunities, compare pools across chains, and inspect APY, TVL, impermanent-loss risk, and reward-emission splits before further due diligence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: APY figures can be stale, protocol-reported, or driven by temporary reward emissions. <br>
Mitigation: Treat scanner output as a shortlist; verify current APY, base-versus-reward composition, pool contracts, and audits on the protocol's own site before allocating capital. <br>
Risk: Stablecoin filtering may misclassify obscure, newly listed, or de-pegged assets. <br>
Mitigation: Review the returned pool symbol, asset composition, TVL, and peg status before using the result for treasury or yield decisions. <br>


## Reference(s): <br>
- [DeFiLlama Yields API](https://yields.llama.fi) <br>
- [DeFiLlama Pools Endpoint](https://yields.llama.fi/pools) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Terminal table or JSON, with command examples in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only output based on public DeFiLlama yield data; no wallet, credential, contract approval, trade, deposit, or withdrawal behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
