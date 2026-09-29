## Description:

Helps parents check their children's SchoolPass arrival and dismissal information and request confirmed dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to review linked students, pickup drivers, school calendars and dismissal locations through their own SchoolPass account, and to request dismissal changes with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration receives parent credentials and access to a child's school logistics.

Mitigation: Install only if you trust the package and environment; never share passwords or session tokens in conversation.

Risk: Dismissal changes can affect a child's actual pickup arrangements.

Mitigation: Keep the default confirmation flow, review each preview, and approve only the intended change; avoid automatic confirmation.

## Reference(s):

- [Schoolpass skill listing](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dismissal-change requests include a preview and require explicit confirmation before submission.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
