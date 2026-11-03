## Description:

Lets an agent draft, preview, publish, schedule, and manage Facebook Page posts through a connected 1Social account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sultanlive](https://clawhub.ai/user/sultanlive)

### License/Terms of Use:

MIT-0

## Use Case:

People managing Facebook Pages can use this skill to draft, preview, schedule, publish, and manage posts through their connected 1Social account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading a local media file makes it publicly accessible before the post is approved.

Mitigation: Show the exact file and get explicit approval before uploading; explain that declining the post will not remove the uploaded file.

Risk: Published posts may be difficult to remove on some selected networks.

Mitigation: Preview the selected destinations and timing, get clear approval before publishing, and report deletion results for each network.

Risk: A delivery result may be unknown, so an unverified retry could publish a duplicate.

Mitigation: Ask the user to check whether the post is live and confirm the result before retrying.

## Reference(s):

- [1Social Facebook publishing guide](https://1social.dev/post-to/facebook?ref=skill)
- [1Social MCP setup](https://1social.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Facebook Page post text, scheduling details, and delivery status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts may include media and can be scheduled up to 30 days ahead.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
