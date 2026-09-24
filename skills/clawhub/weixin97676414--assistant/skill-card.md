## Description:

Xinjianxue Skill Assistant Cn is a Chinese-language custom advisor entry point that helps an agent authenticate with Xinjianxue, request paid feature-code reports, and format guidance using server-returned analysis rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to connect a Xinjianxue account, spend service credits, request time-sensitive report analysis, and receive responses shaped by the user's chosen advisor role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send sensitive personal details to an external paid service and spend service credits.

Mitigation: Install only when the publisher and service are trusted, confirm the user wants to use the service before report calls, and disclose credit usage before paid requests.

Risk: The skill asks the agent to retain reusable account credentials.

Mitigation: Store license and API credentials only in a real secret store or similarly protected host mechanism, and avoid plaintext conversation or memory storage when possible.

Risk: Server-returned report rules can influence response format and safety framing.

Mitigation: Treat server-returned analysis rules as service content that remains subordinate to platform, developer, and safety requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/weixin97676414/skills/assistant)
- [Xinjianxue API Base](https://chinaapi.xinjianxue.com)
- [Xinjianxue MCP Endpoint](https://chinaapi.xinjianxue.com/mcp)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration, markdown]

**Output Format:** [Markdown with JSON and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-binding steps, credential-handling guidance, report summaries, and MCP configuration snippets.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
