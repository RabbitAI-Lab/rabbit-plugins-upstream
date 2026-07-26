## Description: <br>
Query McDonald's China MCP server via the mcd-cn CLI for campaign calendars, coupons, and auto-claiming, with human-readable output or JSON for scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryanchen01](https://clawhub.ai/user/ryanchen01) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to look up McDonald's China campaign calendars and coupons through the mcd-cn CLI and, when intended, trigger coupon claiming for an authenticated account. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The auto-bind-coupons command can claim coupons on the authenticated McDonald's China account. <br>
Mitigation: Run auto-bind-coupons only when coupon claiming is intended and confirm the account context before executing it. <br>
Risk: MCDCN_MCP_TOKEN grants access to the user's McDonald's China MCP account. <br>
Mitigation: Store it as a secret, avoid committing it to .env files, and rotate it if exposed. <br>


## Reference(s): <br>
- [McDonald's China skill page](https://clawhub.ai/ryanchen01/skills/mcd-cn) <br>
- [ryanchen01 publisher profile](https://clawhub.ai/user/ryanchen01) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; the referenced CLI can emit human-readable text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the mcd-cn CLI and MCDCN_MCP_TOKEN.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
