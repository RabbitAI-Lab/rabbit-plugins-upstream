## Description:

This skill should be used when the user asks about their child's school arrival/dismissal through a SchoolPass parent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with SchoolPass parent accounts use this skill to read parent-scoped school arrival and dismissal data and, after explicit confirmation, submit or cancel dismissal changes for their own students.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires persistent SchoolPass parent credentials and can expose parent-scoped student, driver, calendar, and school information.

Mitigation: Use a private user-level MCP configuration with restrictive permissions, avoid shared or committed project configs, and never echo passwords or session tokens.

Risk: Dismissal submit and cancel tools can make real changes affecting student pickup.

Mitigation: Show the dry-run preview to the user and require explicit confirmation before using confirm:true; treat submit and cancel actions as real changes.

Risk: An unverified submitted dismissal change may have been accepted even when the calendar re-read does not confirm it.

Mitigation: Do not resubmit automatically when verified:false is returned; re-read the calendar and ask the user to verify the status.

Risk: Repeated failed login attempts may trigger SchoolPass account challenges.

Mitigation: Run the healthcheck first, separate reachability from authentication failures, and stop after a rejected login rather than retrying guessed credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [npm package: schoolpass-mcp](https://www.npmjs.com/package/schoolpass-mcp)
- [Source listed in skill: schoolpass-mcp](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with JSON configuration snippets and SchoolPass MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include parent account data returned by SchoolPass MCP tools; dismissal-change write tools require explicit confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
