## Description: <br>
Use this skill for Eastmoney MX self-selected stock watchlist management when the user explicitly asks to query, add, or delete stocks in their personal watchlist/self-select list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to query, add, and delete stocks in their Eastmoney self-selected watchlist when they provide an explicit watchlist request. It is not intended for quotes, financial data lookup, news research, stock screening, or simulated trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change account data by adding or deleting stocks in an Eastmoney watchlist through a remote API. <br>
Mitigation: Use mutation actions only after the user explicitly names the action and stock; ask for clarification when the request is ambiguous. <br>
Risk: The skill requires an Eastmoney API key and can read it from configuration. <br>
Mitigation: Prefer setting MX_APIKEY directly in the environment and review installation before granting the skill access to the key. <br>
Risk: The mutation path is broader than the written trigger boundaries describe. <br>
Mitigation: Route only self-selected watchlist query, add, and delete requests to this skill, and keep quote lookup, screening, news research, and simulated trading on their separate skills. <br>


## Reference(s): <br>
- [mx-zixuan Result Fields](references/result-fields.md) <br>
- [ClawHub skill page](https://clawhub.ai/zoeluli7459-dev/skills/mx-zixuan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; query runs can produce CSV and raw JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MX_APIKEY; MX_OUTPUT_DIR can override the default output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
