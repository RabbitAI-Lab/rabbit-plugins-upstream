## Description: <br>
Helps agents find early IT and Xinchuang business opportunities by scanning proposed digital projects, procurement intentions, and expiring service contracts, then ranking leads by value and urgency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, business-development, and IT solution teams use this skill to identify and prioritize early China IT opportunities across Xinchuang, software development, system integration, cloud, cybersecurity, smart-city, and digital-government projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts the Zhiliaobiaoxun service and sends search terms for opportunity lookup. <br>
Mitigation: Use it only when sharing the requested industry, product, region, and budget criteria with that service is acceptable. <br>
Risk: The skill can store an API key under the user's home directory. <br>
Mitigation: Review local credential storage expectations before installation and avoid exposing the API key in chat or reports. <br>
Risk: Trial registration hashes a local MAC address after consent for device de-duplication. <br>
Mitigation: Proceed with automatic registration only after explicit user consent, or configure ZLBX_API_KEY manually to bypass registration. <br>
Risk: Generated sk and auto-login links may allow access without a normal login flow. <br>
Mitigation: Treat generated links and saved HTML reports as sensitive and avoid broad sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/it-project-opportunity-radar) <br>
- [Publisher profile](https://clawhub.ai/user/dragonzu) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Auto-registration flow](artifact/references/auto-register.md) <br>
- [Zhiliaobiaoxun agent portal](https://agent.zhiliaobiaoxun.com) <br>
- [Zhiliaobiaoxun trial and account portal](https://ai.zhiliaobiaoxun.com/?ch=s104) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Analysis, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown opportunity list with optional local HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs ranked opportunity lists, next-step recommendations, source links, data notes, and an optional self-contained HTML report.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
