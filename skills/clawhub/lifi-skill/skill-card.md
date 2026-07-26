## Description: <br>
Uses the LI.FI API for cross-chain and same-chain swaps, bridges, contract calls, route quotes, chain and token validation, transaction request building, and transfer status tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fabriziogianni7](https://clawhub.ai/user/fabriziogianni7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to request LI.FI swap and bridge quotes, prepare transaction requests, handle required approvals through wallet tools, submit supported transactions, and track transfer status with explorer links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can approve tokens and submit real on-chain transactions, including approvals with broad risk defaults. <br>
Mitigation: Before approving or broadcasting, verify chain, token, amount, recipient, slippage, approval amount, and explorer link; avoid unlimited approvals unless intentionally accepted. <br>
Risk: The skill defaults to 10% slippage and requires skipSimulation=true for quotes, which can increase transaction execution risk. <br>
Mitigation: Confirm slippage with the user for each transaction and use a tighter value when appropriate. <br>


## Reference(s): <br>
- [ClawHub LI.FI Skill Listing](https://clawhub.ai/fabriziogianni7/skills/lifi-skill) <br>
- [LI.FI Documentation](https://docs.li.fi/) <br>
- [LI.FI LLM Docs](https://docs.li.fi/llms.txt) <br>
- [LI.FI OpenAPI Specification](https://gist.githubusercontent.com/kenny-io/7fede47200a757195000bfbe14c5baee/raw/725cf9d4a6920d5b930925b0412d766aa53c701c/lifi-openapi.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks, transaction summaries, and block explorer links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LIFI_API_KEY plus user wallet and transaction details; outputs should stay within documented LI.FI endpoints and supported wallet tools.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
