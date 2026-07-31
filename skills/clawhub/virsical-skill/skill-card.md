## Description: <br>
Virsical Skill helps users query or book meeting rooms, view their meetings, query visitor records, and create facility work orders through the Virsical workplace management platform with bilingual Chinese and English responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wafer](https://clawhub.ai/user/wafer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workplace support teams use this skill to manage Virsical office-space workflows from chat, including room availability checks, meeting bookings, visitor lookups, and work-order creation. Developers and operators can use the bundled command references to understand the supported Python entry points and authentication flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles account authorization codes and stores reusable local tokens. <br>
Mitigation: Use it only in a private trusted chat, treat authorization codes and token files as secrets, and log out or clear tokens when access is no longer needed. <br>
Risk: The skill can create live meeting bookings and facility work orders. <br>
Mitigation: Confirm the room, time, title, project, type, priority, and description with the user before executing any booking or work-order creation. <br>
Risk: A misconfigured Virsical base URL could send authentication or business requests to the wrong tenant. <br>
Mitigation: Verify that the configured Virsical base URL is the user's real tenant before login or business operations. <br>
Risk: Visitor queries can reveal personal contact data such as phone numbers. <br>
Mitigation: Run visitor lookups only for legitimate private workplace use and share the minimum visitor details needed for the request. <br>


## Reference(s): <br>
- [Virsical API Reference](references/api_reference.md) <br>
- [Virsical OAuth2 Authentication Flow](references/auth_flow.md) <br>
- [Virsical Commands Reference](references/commands.md) <br>
- [Virsical Error Codes](references/error_codes.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/wafer/skills/virsical-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown tables and lists with inline shell commands and concise status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual Chinese and English responses; raw API JSON is summarized for users.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
