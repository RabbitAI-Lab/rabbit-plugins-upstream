## Description: <br>
Pay for x402-enabled Agent endpoints using TRC20 tokens (USDT/USDD) on TRON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wzc1206](https://clawhub.ai/user/wzc1206) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to invoke x402-enabled agent APIs and complete required TRC20 token payments with USDT or USDD on TRON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically use TRON wallet credentials to spend tokens and create long-lived token approvals. <br>
Mitigation: Use a dedicated low-balance wallet, start on testnet, review each endpoint and price before use, and revoke token approvals after use. <br>
Risk: Mainnet use can expose valuable wallet funds or broad mcporter credentials. <br>
Mitigation: Avoid valuable mainnet keys and broad mcporter credentials; scope credentials to the minimum funds and purpose needed for the intended payments. <br>
Risk: Binary or image responses may be written to temporary files. <br>
Mitigation: Delete temporary response files after they have been inspected or consumed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wzc1206/skills/tron-x402-payment) <br>
- [Publisher profile](https://clawhub.ai/user/wzc1206) <br>
- [x402 protocol](https://x402.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; tool execution returns JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save binary or image endpoint responses to temporary files and return their file paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter declares 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
