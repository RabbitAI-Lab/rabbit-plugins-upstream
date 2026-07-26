## Description: <br>
Trade Ostium RWA perps on Arbitrum via CAI using market lookup, preflight checks, trade placement, order status polling, and hosted enrollment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bernardtai](https://clawhub.ai/user/bernardtai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to prepare, place, monitor, and close CAI-managed Ostium perpetual trades on Arbitrum. It guides enrollment, API key setup, collateral checks, preflight validation, and order status review before live trading actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent place real-money perpetual trades through CAI/Ostium. <br>
Mitigation: Require clear user confirmation of collateral, pair, leverage, direction, order type, and close action before any live trade is submitted. <br>
Risk: A CAI API key with platform or full scope may permit sensitive trading actions. <br>
Mitigation: Confirm the intended CAI_API_KEY scope, keep permissions limited where possible, and store the key only through the configured secrets mechanism. <br>
Risk: Incorrect market identifiers or unsupported platform readiness can cause failed or unintended trade flows. <br>
Mitigation: Resolve pair_id through defi_markets, run defi_preflight until valid, and address platform_readiness blocking reasons before trade placement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bernardtai/skills/ostium-with-cai) <br>
- [CAI skill reference](https://cai.com/skill.md) <br>
- [CAI tools manifest](https://cai.com/specs/cai-tools.manifest.json) <br>
- [CAI developer documentation](https://cai.com/developers.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline command examples and structured API parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a CAI_API_KEY with platform or full scope and explicit confirmation before live trade placement.] <br>

## Skill Version(s): <br>
1.0.18 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
