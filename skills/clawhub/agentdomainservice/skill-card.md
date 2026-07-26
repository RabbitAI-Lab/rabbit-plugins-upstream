## Description: <br>
Domain availability API for AI agents to check single domains, explore names across TLDs, filter by budget, and get smart suggestions with JSON or TXT responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gregm711](https://clawhub.ai/user/gregm711) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and AI agents use this skill to look up domain availability, quote and purchase domains, and configure DNS, nameservers, transfer, recovery, and domain settings through the ClawDaddy API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through real domain purchases and payment flows. <br>
Mitigation: Require explicit user approval for quotes, purchases, payment proofs, and checkout links before execution. <br>
Risk: The skill can guide DNS edits, nameserver updates, transfers, recovery, and settings changes that affect live domain control. <br>
Mitigation: Review the exact target domain, requested records, nameservers, transfer action, or settings change before applying it. <br>
Risk: Management tokens grant control over domains and may appear in responses or agent output. <br>
Mitigation: Treat management tokens as passwords, avoid logging or sharing them, and rotate or recover tokens if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gregm711/skills/agentdomainservice) <br>
- [ClawDaddy](https://clawdaddy.app) <br>
- [ClawDaddy agent documentation](https://clawdaddy.app/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP requests and JSON or TXT response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include domain-management tokens or payment flow details that should be treated as sensitive.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
