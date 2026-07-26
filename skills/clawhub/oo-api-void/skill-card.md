## Description: <br>
APIVoid (apivoid.com). Use this skill for ANY APIVoid request: searching and reading data through the OOMOL APIVoid connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query APIVoid reputation, blacklist, risk, verification, and account-usage data through an OOMOL-connected account. It is intended for domain, IP, URL, and email reputation workflows where the agent should inspect the live connector schema before running an action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run APIVoid connector actions through an authenticated OOMOL account, including account usage lookup and reputation checks that may depend on account credit. <br>
Mitigation: Use an account with appropriately scoped access, review connector schemas before execution, and stop when APIVoid or OOMOL reports insufficient credit or connection problems. <br>
Risk: APIVoid results may influence security or reputation decisions for domains, IPs, URLs, and email addresses. <br>
Mitigation: Treat returned reputation and risk signals as decision support and validate high-impact actions with additional context before acting. <br>


## Reference(s): <br>
- [APIVoid homepage](https://www.apivoid.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub APIVoid skill page](https://clawhub.ai/oomol/skills/oo-api-void) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to fetch the live connector schema before constructing action payloads and to return APIVoid responses from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
