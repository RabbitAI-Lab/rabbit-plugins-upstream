## Description:

Helps agents find AllTrails hiking routes and read trail details, reviews, photos, weather, and signed-in account activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and agents assisting them can search for trails, compare route details and reviews, and retrieve saved lists or completed hikes when the user requests access to their account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial integration relies on a signed-in browser session and may expose account details to the agent.

Mitigation: Review the package and browser extension before installation; use profile, saved-list, completed-trail, and activity tools only when account access is intended.

Risk: Broad hiking-related triggers may activate the integration unexpectedly.

Mitigation: Confirm the user wants AllTrails data before accessing the signed-in session, especially for personal information.

Risk: Unofficial access can break or conflict with AllTrails terms.

Mitigation: Review applicable terms, consider pinning package and extension versions, and verify trail information before relying on it.

## Reference(s):

- [ClawHub alltrails release](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp npm package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source](https://github.com/chrischall/alltrails-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, GPX route data]

**Output Format:** [Markdown or text; GPX 1.1 for exported routes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trail results are compact by default; full records and route geometry are available on request.]

## Skill Version(s):

3.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
