## Description: <br>
Before completing a purchase, payment, checkout, or subscription on the user's behalf, this skill checks the purchase with Watchpost for merchant trustworthiness, listing manipulation, and the user's spending rules, then proceeds only when Watchpost approves. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lelis92](https://clawhub.ai/user/lelis92) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agentskills-compatible runtimes use Watchpost to gate purchases made on a user's behalf. It prompts setup when the required Watchpost token is missing, sends purchase details for a verdict, and prevents payment when Watchpost blocks, requests review, or cannot complete the check. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill shares purchase details and the user's Watchpost connection token with Watchpost to obtain a purchase verdict. <br>
Mitigation: Install only when the user is comfortable sharing purchase details with Watchpost, and configure WATCHPOST_TOKEN from the user's Watchpost account. <br>
Risk: Purchases may be delayed or blocked when WATCHPOST_TOKEN is missing, the plan limit is reached, Watchpost requests review, or the check cannot complete. <br>
Mitigation: Treat these states as fail-closed conditions: do not pay until setup is fixed, the allowance is upgraded or reset, or the user explicitly approves a review case. <br>


## Reference(s): <br>
- [Watchpost homepage](https://watchpost.systems/?ref=clawhub) <br>
- [Watchpost ClawHub listing](https://clawhub.ai/lelis92/skills/watchpost) <br>
- [Watchpost signup](https://app.watchpost.systems/signup?ref=clawhub) <br>
- [Watchpost agent connections](https://app.watchpost.systems/connections?ref=clawhub) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON helper output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 20 or newer, network access to api.watchpost.systems, and WATCHPOST_TOKEN. The helper returns purchase decisions through JSON output and exit codes.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata, skill frontmatter, artifact README) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
