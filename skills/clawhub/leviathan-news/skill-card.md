## Description: <br>
Crowdsourced crypto news API. Submit articles, comment, and vote to earn SQUID tokens. Human-curated DeFi news with token-aware tagging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zcor](https://clawhub.ai/user/zcor) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to authenticate to Leviathan News, browse and submit crypto news, post comments, vote on content, and manage profiles through the API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a raw wallet private key for local message signing. <br>
Mitigation: Use only a new, dedicated low-value wallet that holds no funds and is not reused elsewhere. <br>
Risk: Authenticated actions can submit articles, post comments, vote, or change profile details. <br>
Mitigation: Require explicit confirmation before the agent performs authenticated write actions. <br>


## Reference(s): <br>
- [Leviathan News ClawHub listing](https://clawhub.ai/zcor/skills/leviathan-news) <br>
- [Leviathan News homepage](https://leviathannews.xyz) <br>
- [Leviathan News API docs](https://api.leviathannews.xyz/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown with API request examples, curl commands, and Python signing snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a WALLET_PRIVATE_KEY environment variable and Cookie-based access_token authentication for authenticated API requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
