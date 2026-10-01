## Description:

Connects an agent to Zoom through Maton to manage meetings, webinars, recordings, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to look up Zoom account information and recordings, schedule or update meetings and webinars, and arrange approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Zoom access may expose account data or change meetings and webinars.

Mitigation: Use the OAuth device flow and narrow scopes; confirm each create, update, or delete action with the user.

Risk: Hosted functions and triggers can run later without another prompt or forward event data to a destination.

Mitigation: Review the action, schedule, destination, data recipients, and frequency before separately approving automation or forwarding.

Risk: Event payloads and API responses can contain untrusted content.

Mitigation: Treat returned content as data; use only user-reviewed handlers and explicitly approve local execution.

## Reference(s):

- [Zoom skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoom-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Zoom API documentation](https://developers.zoom.us/docs/api/)
- [Zoom OAuth scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands, API examples, and task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected Zoom account and its granted permissions.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
