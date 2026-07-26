## Description: <br>
Access AIKEK APIs for crypto/DeFi research and image generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vvsotnikov](https://clawhub.ai/user/vvsotnikov) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to authenticate with AIKEK, query crypto and DeFi research endpoints, generate images, and manage API credits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Solana wallet private key and a non-expiring AIKEK API token stored locally. <br>
Mitigation: Use a secrets vault or restricted local credentials file, keep ~/.config/aikek/credentials private, never print or share the full token, and send credentials only to api.alphakek.ai. <br>
Risk: AIKEK API calls can spend credits and referral submissions may disclose external post URLs. <br>
Mitigation: Review and explicitly approve credit-spending requests and referral verification submissions before running them. <br>
Risk: The generated authentication wallet could be mistaken for a funded wallet. <br>
Mitigation: Use the generated wallet only for AIKEK API authentication and do not put funds in it. <br>


## Reference(s): <br>
- [AIKEK Developer API Documentation](https://docs.alphakek.ai/developers/developer-api.md) <br>
- [AIKEK API Base URL](https://api.alphakek.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/vvsotnikov/skills/aikek) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with bash, Python, curl, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes endpoint examples, credential setup steps, and security notes for AIKEK API use.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
