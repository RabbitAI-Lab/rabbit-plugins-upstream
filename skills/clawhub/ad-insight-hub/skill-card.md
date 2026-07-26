## Description: <br>
Ad Insight Hub helps agents query the AdMapix advertising intelligence API for ad creative search, app and developer profiles, store rankings, and download or revenue estimates with cache-aware endpoint orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, user acquisition, and market analysis teams use this skill through an agent to translate advertising research questions into AdMapix API calls and return structured ad intelligence for competitor creative monitoring, app and developer research, store ranking checks, and regional strategy comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses command execution and network access for curl-style AdMapix API calls. <br>
Mitigation: Review proposed API calls before execution and install the skill only when AdMapix access is intended. <br>
Risk: An AdMapix API key could be exposed if pasted into chat, logs, or URLs. <br>
Mitigation: Configure ADMAPIX_API_KEY as an environment variable and avoid printing, logging, or sharing the key. <br>
Risk: Advertising intelligence data may remain in local cache directories. <br>
Mitigation: Review or delete ~/.admapix-cache when cached data should not remain on the machine. <br>
Risk: Download and revenue outputs are third-party estimates and may be unreliable for long-tail markets. <br>
Mitigation: Treat estimates as directional, preserve the skill's A/B/C confidence labels, and avoid relying on them as sole financial evidence. <br>


## Reference(s): <br>
- [Ad Insight Hub on ClawHub](https://clawhub.ai/thcjp/skills/ad-insight-hub) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [AdMapix](https://www.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash/curl commands and structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ADMAPIX_API_KEY, may use ~/.admapix-cache, and labels download or revenue estimates with A/B/C confidence guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
