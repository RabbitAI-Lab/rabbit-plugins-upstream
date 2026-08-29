## Description:

Query alltrails.com for trail search, trail detail, reviews, photos, weather, and signed-in user data from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell commands and request patterns for read-only AllTrails trail, review, photo, weather, saved-list, completed-trail, and activity-feed lookups. It is intended for workflows that need AllTrails data without installing or running the alltrails-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in AllTrails browser session to access internal endpoints, which can expose personal profile, saved-list, completed-trail, and activity-feed data.

Mitigation: Use it only with an account and browser session you are authorized to use, avoid logging or sharing returned personal data, and keep requests read-only.

Risk: Persistent browser pairing and the global fpx CLI create privileged access that may remain available after initial setup.

Mitigation: Review active pairings and revoke browser or CLI access when the workflow is no longer needed.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only API request guidance that depends on a signed-in AllTrails browser session and captured request headers.]

## Skill Version(s):

2.1.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
