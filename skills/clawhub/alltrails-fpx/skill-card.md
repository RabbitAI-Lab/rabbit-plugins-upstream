## Description:

Provides shell-based guidance for retrieving AllTrails trail and account data through a user's browser session using fpx, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve trail details, reviews, photos, weather, and authorized account activity from AllTrails using shell commands and an active browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using a signed-in browser session may expose personal account and profile data beyond the intended task.

Mitigation: Use account endpoints only for your own data or data you are authorized to access; revoke browser site access or pairing when no longer needed.

Risk: Repeated account or profile queries could enable bulk scraping.

Mitigation: Avoid bulk profile scraping and keep requests limited to authorized tasks.

## Reference(s):

- [AllTrails fpx endpoint examples](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only endpoint examples; raw route geometry rather than GPX output.]

## Skill Version(s):

3.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
