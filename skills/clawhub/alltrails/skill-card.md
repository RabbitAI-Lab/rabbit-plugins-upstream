## Description:

Helps agents find AllTrails hiking routes and read trail details, reviews, photos, weather, and a signed-in user's hiking activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Hikers and travel planners use this skill to discover trails and compare route details, reviews, photos, and weather. Signed-in users can also review their own saved lists and completed hikes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-scoped tools can disclose saved lists, hiking history, or personal profile fields, especially in full-view results.

Mitigation: Use account-scoped tools only for the signed-in user's own requests and prefer compact results unless additional fields are needed.

Risk: The unofficial integration uses an internal AllTrails API and a signed-in browser bridge; automated access may conflict with AllTrails terms or stop working.

Mitigation: Review the applicable terms and use the integration only if comfortable with its unofficial status and browser-extension requirements.

## Reference(s):

- [AllTrails skill on ClawHub](https://clawhub.ai/chrischall/skills/alltrails)
- [alltrails-mcp package](https://www.npmjs.com/package/alltrails-mcp)
- [alltrails-mcp source linked by the skill](https://github.com/chrischall/alltrails-mcp)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, GPX route data, Configuration guidance]

**Output Format:** [Natural-language trail guidance and structured tool results; GPX 1.1 for route exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact results by default; full records and route geometry are available on request.]

## Skill Version(s):

3.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
