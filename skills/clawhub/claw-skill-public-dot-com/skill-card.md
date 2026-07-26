## Description: <br>
Interact with your Public.com brokerage account using the Public.com API to view portfolio data, get quotes, place trades, and get account updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tarricsookdeo](https://clawhub.ai/user/tarricsookdeo) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
External users with a Public.com account use this skill to review account, portfolio, market, and options data, then preflight, submit, or cancel brokerage orders through the Public.com API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access brokerage account data and place or cancel real orders. <br>
Mitigation: Install only when the agent should access the Public.com account, and require explicit user confirmation before every live trade or automated strategy. <br>
Risk: Public.com API credentials enable high-impact account operations. <br>
Mitigation: Run the skill in an isolated environment and keep the API secret tightly scoped in secure configuration. <br>
Risk: The skill depends on the Public.com Python SDK for brokerage API actions. <br>
Mitigation: Preinstall and review the SDK dependency where possible before enabling the skill. <br>


## Reference(s): <br>
- [Public.com API Settings](https://public.com/settings/v2/api) <br>
- [Public.com Signup](https://public.com/signup) <br>
- [Options Automation Playbook](artifact/options-automation-library.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations and summarized command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Public.com API secret and, for account-specific actions, an account ID.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
