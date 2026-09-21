## Description:

This skill helps agents answer questions about a parent's SchoolPass account, including student arrival and dismissal details, authorized pickup drivers, dismissal locations, and pickup changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use this skill through an agent to read SchoolPass account information, check student dismissal calendars, list authorized pickup drivers, and manage pickup or dismissal changes with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SchoolPass parent account and can expose sensitive child, school, pickup, and dismissal information.

Mitigation: Install it only where that account access is appropriate, keep use parent-scoped, and avoid sharing returned student or dismissal details beyond the authorized user.

Risk: SchoolPass credentials and session tokens could be exposed if copied into shared project files or echoed into conversation.

Mitigation: Use private/global MCP configuration or secure secret injection, and never echo passwords or session tokens in agent responses.

Risk: Dismissal-change tools can alter a child's real pickup or arrival plan.

Mitigation: Show the dry-run preview, obtain explicit user approval, and only submit when confirm:true is provided.

Risk: Repeated failed login attempts may trigger account challenges because SchoolPass login is protected by reCAPTCHA.

Mitigation: Stop after a rejected login and ask the user to verify email, password, and school code instead of retrying guesses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured tool guidance with JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses may be compact or full; dismissal-change writes require a preview and explicit confirm:true before submission.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
