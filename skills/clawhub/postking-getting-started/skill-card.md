## Description: <br>
First-run flow for PostKing: authenticate, top up credits, onboard a brand from a URL, connect socials, and ship a first post. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bitsandtea](https://clawhub.ai/user/bitsandtea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External PostKing users and agents use this skill as the first-run onboarding path: checking authentication, funding credits, creating or selecting a brand, connecting social accounts, and scheduling an initial post. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Funding steps may charge a saved card immediately or start a recurring subscription after checkout. <br>
Mitigation: Confirm the exact pack, tier, interval, and expected charge with the user before calling billing tools. <br>
Risk: Social connection steps can link a PostKing brand to an external social account. <br>
Mitigation: Ask which platform to connect and wait for the user to complete and confirm the OAuth flow. <br>
Risk: Brand onboarding can crawl a website and generate brand themes from user-provided details. <br>
Mitigation: Confirm the brand name and website URL in the current conversation before onboarding. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/bitsandtea/skills/postking-getting-started) <br>
- [PostKing MCP endpoint](https://mcp.postking.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls] <br>
**Output Format:** [Markdown guidance with staged tool calls and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [One onboarding stage per turn; user confirmation is required before billing, brand, social account, and post-scheduling decisions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
