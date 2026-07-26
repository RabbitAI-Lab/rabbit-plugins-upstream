## Description: <br>
Call real paid data APIs for web search, scraping, SEO/SERP, finance data, and LLM access through SettleMesh with per-call metering and upfront cost quotes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover, quote, and call paid live-data capabilities without separately managing each vendor relationship. It is aimed at workflows that need current web, scraping, SEO/SERP, market, or LLM data with visible per-call cost before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate authenticated, metered data calls that may spend account balance. <br>
Mitigation: Require explicit confirmation before paid or side-effecting calls and review quotes before execution. <br>
Risk: The skill directs agents to start and cache a SettleMesh login session automatically. <br>
Mitigation: Prefer a user-provided SETTLE_API_KEY or manually approve login after confirming the account and billing context. <br>


## Reference(s): <br>
- [Metered Data Fetch on ClawHub](https://clawhub.ai/structureintelligence/skills/metered-data-fetch) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the settlemesh CLI and SETTLE_API_KEY for authenticated network calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
