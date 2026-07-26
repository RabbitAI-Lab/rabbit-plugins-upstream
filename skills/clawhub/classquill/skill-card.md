## Description: <br>
Query a ClassQuill tutoring business, including sessions, students, tutors, parents, invoices, payments, lesson plans, bookings, earnings, and reports, through the ClassQuill MCP server or public API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brandoncollis](https://clawhub.ai/user/brandoncollis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tutoring business operators and their agents use this skill to retrieve live, read-only ClassQuill operational data for scheduling, billing, student and tutor lookup, lesson plans, homework, earnings, and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill retrieves live, organization-scoped tutoring business data through a bearer API key or OAuth. <br>
Mitigation: Use scoped credentials where available, keep EQUATEIT_API_KEY private, and only enable the skill for agents that should access the ClassQuill organization. <br>
Risk: Agent summaries of live operational, billing, or student data may be incomplete or misleading if based on the wrong endpoint or stale context. <br>
Mitigation: Call the relevant ClassQuill tool for current data and review summaries before relying on them for scheduling, billing, or customer communication. <br>
Risk: Local setup can execute the equateit-mcp package through npx. <br>
Mitigation: Use the hosted MCP server when appropriate, or review the local package and runtime environment before running npx in trusted systems. <br>


## Reference(s): <br>
- [Classquill on ClawHub](https://clawhub.ai/brandoncollis/skills/classquill) <br>
- [ClassQuill MCP server](https://mcp.classquill.com/mcp) <br>
- [ClassQuill public API](https://api.classquill.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown or plain-language text with optional inline shell commands and API-derived summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only, organization-scoped access requires EQUATEIT_API_KEY or supported OAuth authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
