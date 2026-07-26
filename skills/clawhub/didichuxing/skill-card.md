## Description: <br>
Didichuxing is a DiDi ride-hailing decision guide for product selection, fare estimation, peak-hour travel strategies, and enterprise API and ride-rule configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to compare DiDi ride options, estimate fare ranges, plan around peak demand or weather, and prepare enterprise ride-management rules or API integration examples. <br>

### Deployment Geography for Use: <br>
Global, with examples focused on DiDi ride-hailing scenarios and Chinese city pricing assumptions. <br>

## Known Risks and Mitigations: <br>
Risk: Fare estimates and ride recommendations may differ from live DiDi app prices because pricing varies by city, time, demand, weather, route, and fees. <br>
Mitigation: Treat outputs as planning guidance, present ranges rather than fixed prices, and confirm final quotes in the DiDi app before booking. <br>
Risk: Enterprise API examples involve client secrets and sensitive rider, location, token, and billing data. <br>
Mitigation: Use the examples only with authorized DiDi Enterprise access, store secrets in a secrets manager, avoid logging sensitive data, and apply consent, retention, and regional privacy requirements. <br>
Risk: Travel advice can affect personal safety in late-night, remote, severe-weather, or high-demand situations. <br>
Mitigation: Include safety reminders such as sharing trip status, using emergency contacts, and preferring safer public or official transport options when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhangifonly/skills/didichuxing) <br>
- [DiDi Open Platform](https://open.didichuxing.com) <br>
- [DiDi Enterprise Console](https://es.xiaojukeji.com) <br>
- [DiDi Enterprise API endpoint](https://api.es.xiaojukeji.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Configuration] <br>
**Output Format:** [Markdown with tables, prose recommendations, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fare estimates are approximate ranges and enterprise API examples require authorized DiDi Enterprise access plus proper secrets and sensitive-data handling.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
