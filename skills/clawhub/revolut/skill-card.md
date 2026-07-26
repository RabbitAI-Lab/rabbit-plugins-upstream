## Description: <br>
Revolut web automation via Playwright: login/logout, list accounts, and fetch transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and finance operators use this skill to automate an authenticated Revolut web session and export account balances, wallet transactions, investment portfolio holdings, and investment transactions as JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates an authenticated Revolut web banking session and stores browser session data under workspace/revolut. <br>
Mitigation: Run it only in a private workspace, treat workspace/revolut as sensitive banking session data, and use logout after each session. <br>
Risk: An optional app PIN can be stored in config.json. <br>
Mitigation: Avoid storing the PIN unless necessary and restrict access to the configuration file. <br>
Risk: Exported JSON can contain sensitive account, transaction, and portfolio data. <br>
Mitigation: Keep exported files out of shared folders and backups, and write outputs only to trusted workspace or /tmp paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/odrobnik/skills/revolut) <br>
- [Publisher profile](https://clawhub.ai/user/odrobnik) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON output and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Playwright with Chromium and an authenticated Revolut session; optional --out writes JSON under the workspace or /tmp.] <br>

## Skill Version(s): <br>
1.3.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
