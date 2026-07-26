## Description: <br>
Complete Kimai time-tracking API integration. Manage timesheets, customers, projects, activities, teams, invoices and exports via REST API. Supports time tracking workflows, reporting, and administrative operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0x7466](https://clawhub.ai/user/0x7466) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, administrators, and time-tracking users use this skill to manage Kimai timesheets, customers, projects, activities, teams, invoices, exports, and system checks from an agent-assisted CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Kimai API token that can read or change records on the configured Kimai server. <br>
Mitigation: Use a least-privilege token and confirm KIMAI_BASE_URL points to the intended trusted Kimai instance before running commands. <br>
Risk: Delete operations and forced actions can modify or remove Kimai records. <br>
Mitigation: Reserve --force and delete operations for explicit, reviewed requests; rely on confirmation prompts for destructive actions. <br>
Risk: Timesheet and export data may contain sensitive business or personal information. <br>
Mitigation: Keep exports in a controlled workspace and redact personal data before sharing command output or debug logs. <br>


## Reference(s): <br>
- [Kimai REST API Docs](https://www.kimai.org/documentation/rest-api.html) <br>
- [Kimai API Pagination Guide](https://www.kimai.org/documentation/api-pagination.html) <br>
- [Kimai Project Website](https://www.kimai.org/) <br>
- [ClawHub Skill Page](https://clawhub.ai/0x7466/skills/kimai-time-tracking) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, CSV] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus JSON, table, or CSV command output from the Kimai CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KIMAI_BASE_URL and KIMAI_API_TOKEN for live Kimai API operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
