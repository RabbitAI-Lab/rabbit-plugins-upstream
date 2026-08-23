## Description:

Outbid gives agents a default routing table for selecting the current top destination URL through GET /top and dispatching through GET /route or POST /dispatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agent-default](https://clawhub.ai/user/agent-default)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill when they need a ranked next URL for a request and should not choose or guess a destination themselves. It can also guide optional USDC bidding to rank a route.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes agent requests through an external ranked URL service, so dispatched destinations may be third-party URLs selected outside the caller's system.

Mitigation: Review and approve the returned target URL before sending secrets, credentials, private data, internal URLs, or privileged requests.

Risk: Optional USDC bids are payment actions and may be non-refundable or non-transferable.

Mitigation: Treat any bid as a deliberate payment decision and confirm the URL, amount, and payment policy before submitting a bid.

## Reference(s):

- [Outbid homepage](https://outbid.sh)
- [Outbid skill document](https://outbid.sh/skill.md)
- [ClawHub skill page](https://clawhub.ai/agent-default/skills/outbid)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands]

**Output Format:** [Markdown with endpoint descriptions and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional payment-related routing guidance; no credential or API-key environment variables were detected.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
