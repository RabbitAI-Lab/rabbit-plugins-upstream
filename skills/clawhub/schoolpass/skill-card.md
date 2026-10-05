## Description:

Helps parents check their children's SchoolPass arrival and dismissal details and request confirmed pickup changes through their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to review linked students, arrival and dismissal schedules, authorized drivers, and pickup changes in their SchoolPass account. They can also request a dismissal change or cancellation after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parent credentials and private child or family information may be exposed through shared configuration or unnecessarily detailed responses.

Mitigation: Use a private MCP configuration and a secrets manager where available; avoid sharing credentials, session tokens, or unnecessary full records.

Risk: Submitting or canceling a dismissal change can alter a child's real pickup arrangements.

Mitigation: Show the exact proposed change and obtain explicit parent approval before submitting; if submission status is uncertain, recheck the calendar rather than retrying.

Risk: Running an unpinned external MCP package through npx can introduce unexpected code changes.

Mitigation: Confirm the npm package source and version before installation or execution.

## Reference(s):

- [schoolpass ClawHub listing](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package listed in skill documentation](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain private student and family information; dismissal changes require confirmation.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
