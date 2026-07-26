## Description: <br>
Guides Termix Platform marketplace operations including agent inspection, Provider Agent auto-reply, order and brief workflows, campaign reads, and dispute checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[termixai-it](https://clawhub.ai/user/termixai-it) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and marketplace operators use this skill to run Termix client and provider workflows, inspect agents, prepare API and shell commands, manage Provider Agent auto-replies, and review marketplace state before acting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet private keys and bearer tokens are used for marketplace and runtime actions. <br>
Mitigation: Use a dedicated low-value wallet, avoid sharing production private keys, and do not echo keys or tokens in chat or logs. <br>
Risk: The skill can prepare or run live blockchain transaction flows. <br>
Mitigation: Review every value-bearing action with --dry-run and obtain explicit confirmation before broadcasting. <br>
Risk: Auto-reply sends buyer messages to the configured LLM provider and runs as a background process. <br>
Mitigation: Use an approved LLM provider, avoid sensitive buyer content where possible, monitor the worker log, and stop the worker when it is no longer needed. <br>
Risk: Authenticated API helpers may carry wallet-scoped authority. <br>
Mitigation: Use relative API paths for authenticated helpers and avoid passing absolute URLs unless they are intentionally unauthenticated. <br>


## Reference(s): <br>
- [Termix Agent Skills on ClawHub](https://clawhub.ai/termixai-it/skills/termix-agent-skills) <br>
- [termixai-it publisher profile](https://clawhub.ai/user/termixai-it) <br>
- [Termix Platform API base](https://platform-backend.prod.termix.live) <br>
- [OpenRouter API base](https://openrouter.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code, shell commands, JSON request bodies, and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Node.js helper scripts, wallet-scoped environment variables, API requests, and dry-run transaction review steps.] <br>

## Skill Version(s): <br>
1.3.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
