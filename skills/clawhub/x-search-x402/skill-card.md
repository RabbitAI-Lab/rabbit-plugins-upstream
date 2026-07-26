## Description: <br>
AI-powered X/Twitter search for real-time trends, breaking news, sentiment analysis, and social media insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tzannetosgiannis](https://clawhub.ai/user/tzannetosgiannis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for current X/Twitter trends, hashtags, viral posts, sentiment, breaking news, and public opinion signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to store and pass a raw wallet private key to an unpinned third-party npm tool. <br>
Mitigation: Use a dedicated low-balance Base wallet, avoid reusing a primary wallet private key, prefer environment-based secret handling over plaintext config files, and review or pin the npm package before use. <br>
Risk: Each successful search can trigger a paid x402 request. <br>
Mitigation: Confirm the query and wallet balance before running searches, and monitor Base USDC spend for repeated or automated use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tzannetosgiannis/skills/x-search-x402) <br>
- [Publisher profile](https://clawhub.ai/user/tzannetosgiannis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Text or Markdown responses with shell command and configuration guidance when setup or errors require it.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search requests may require a configured x402 private key and incur a $0.05 USDC payment on Base per request.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
