## Description:

Query alltrails.com for trail search, trail detail, reviews, photos, weather, and signed-in user data from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to make read-only AllTrails queries from shell workflows when the AllTrails MCP server is unavailable, unnecessary, or not installed. It supports trail lookup, reviews, photos, weather, route geometry, and account-linked saved lists, completed trails, and activity feeds when the user is signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read account-linked AllTrails data through a signed-in browser tab, including saved lists, completed trails, and activity feeds.

Mitigation: Use per-user commands only with the account holder's permission and treat returned AllTrails data as personal data.

Risk: The fpx and Transporter pairing can persist after initial approval.

Mitigation: Review and remove the pairing when this access is no longer needed.

Risk: AllTrails responses can fail or return an interstitial page when the signed-in tab, captured app key, or DataDome state is stale.

Mitigation: Refresh or reopen the signed-in AllTrails tab, recapture the x-at-key header, and verify that responses are valid JSON before using them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx)
- [AllTrails endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide read-only fpx requests through the user's browser session; callers should inspect JSON bodies and handle AllTrails or DataDome interstitial responses.]

## Skill Version(s):

2.2.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
