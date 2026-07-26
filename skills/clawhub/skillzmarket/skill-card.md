## Description: <br>
Search and call monetized AI skills from Skillz Market with automatic USDC payments on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hiich](https://clawhub.ai/user/hiich) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to discover Skillz Market services, inspect service details, and call paid external AI skills with x402 USDC payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured wallet key can authorize USDC payments for paid skill calls. <br>
Mitigation: Use a dedicated low-balance wallet and review the destination service and expected price before making paid calls. <br>
Risk: The direct command can send paid requests and request JSON to arbitrary x402-enabled endpoints. <br>
Mitigation: Avoid direct calls unless the endpoint is trusted, and do not include secrets or sensitive data in request JSON. <br>


## Reference(s): <br>
- [ClawHub SkillzMarket release page](https://clawhub.ai/hiich/skills/skillzmarket) <br>
- [Skillz Market](https://skillz.market) <br>
- [x402 Protocol](https://x402.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON responses and plain-text CLI status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and info commands return Skillz Market data; paid calls return responses from external x402-enabled endpoints.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
