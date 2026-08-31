## Description:

This skill helps agents use a parent-scoped SchoolPass MCP server to read student arrival and dismissal information and prepare confirm-gated pickup or dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and assisting agents use this skill to check students, calendars, pickup drivers, dismissal locations, school information, and pending pickup changes through a SchoolPass parent account. It can also guide explicitly confirmed dismissal-change submissions or cancellations after preview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses SchoolPass parent credentials and can access a child's dismissal, pickup, driver, and school information.

Mitigation: Install only when that account access is acceptable, keep credentials and session tokens out of conversation output, and limit use to the user's own parent account.

Risk: Confirmed dismissal-change tools can alter a real school pickup or arrival plan.

Mitigation: Show the preview first and approve confirm:true only after the user explicitly confirms the intended change.

Risk: Repeated rejected SchoolPass logins can lead to account challenges because SchoolPass fronts login with reCAPTCHA.

Mitigation: Stop after a rejected login and ask the user to verify the email, password, and school code instead of retrying guesses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SchoolPass MCP tool-call guidance, setup configuration, and user-confirmation prompts before real dismissal changes.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
