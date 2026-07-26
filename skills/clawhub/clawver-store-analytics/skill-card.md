## Description: <br>
Monitor Clawver store performance by querying revenue, top products, conversion rates, growth trends, performance reports, and business analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Store owners, operators, and developers use this skill to retrieve and interpret Clawver store analytics, including revenue, orders, product performance, reviews, and conversion trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses CLAW_API_KEY to access Clawver store analytics, so an overprivileged or exposed key could reveal sensitive store metrics. <br>
Mitigation: Use a least-privilege, preferably read-only key, keep it out of logs, and confirm requests go only to api.clawver.store. <br>
Risk: Analytics may be misreported if unsupported periods are used or cent-denominated revenue fields are treated as dollars. <br>
Mitigation: Use documented period values and divide cent-based money fields by 100 before presenting currency amounts. <br>


## Reference(s): <br>
- [Clawver Store](https://clawver.store) <br>
- [Store Analytics API Examples](references/api-examples.md) <br>
- [ClawHub skill listing](https://clawhub.ai/nwang783/skills/clawver-store-analytics) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with curl commands, JSON response examples, Python snippets, and concise analytics guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY and should send requests only to api.clawver.store.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
