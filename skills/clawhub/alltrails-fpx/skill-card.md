## Description:

Query AllTrails trail data, reviews, photos, weather, and signed-in account lists or activity from a shell through fpx using a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable end users use this skill to make read-only AllTrails queries from shell scripts or an agent when they need trail, search, review, photo, weather, saved-list, completed-trail, or activity-feed data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent read account-specific AllTrails data through a signed-in browser tab.

Mitigation: Use it only for specific requested queries, treat returned account data as personal, and avoid exposing results in shared logs or transcripts.

Risk: Browser pairing may remain available after setup.

Mitigation: Remove or disable the fpx/Transporter pairing when the task is complete or when the agent no longer needs AllTrails access.

Risk: The skill depends on live captured request headers and a signed-in tab, so stale headers or an uncleared browser challenge can produce failed or misleading responses.

Mitigation: Re-capture the app header before retrying failed calls and verify that returned bodies are valid JSON before using the data.

## Reference(s):

- [AllTrails endpoints for fpx](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with shell command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails GET and read POST workflows; signed-in account endpoints may return personal data.]

## Skill Version(s):

3.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
