## Description: <br>
Harvest Time Reporting helps agents use the Harvest API to manage time entries, projects, tasks, clients, users, invoices, expenses, reports, and related account records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zachgodsell93](https://clawhub.ai/user/zachgodsell93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and agent users can use this skill to connect an agent to a Harvest account for time tracking, reporting, and account-management workflows. It is most useful when an agent needs Harvest API setup guidance, endpoint references, and example shell commands for supported operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A powerful Harvest access token can affect real business data, including time entries, projects, users, invoices, payments, roles, and company settings. <br>
Mitigation: Use the least-privileged Harvest token available and require explicit human review before create, update, delete, invoice, payment, role, user, or company-setting actions. <br>
Risk: Credentials or account identifiers could be exposed if users paste tokens into prompts, logs, or generated examples. <br>
Mitigation: Provide Harvest tokens through environment variables or secret storage, and avoid including credentials in chats, logs, or committed files. <br>
Risk: Testing against production Harvest data can unintentionally change client, invoice, expense, or reporting records. <br>
Mitigation: Validate workflows against non-production or low-risk data before allowing actions on production accounts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zachgodsell93/skills/harvest-time-reporting-api) <br>
- [Harvest Developer Portal](https://id.getharvest.com/developers) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Harvest API authentication setup, endpoint examples, query parameters, and pagination and rate-limit notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
