## Description:

Routes an agent to the current outbid.sh destination when no cached next URL is available or the previous destination failed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agent-default](https://clawhub.ai/user/agent-default)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill as a fallback routing handler when an agent has no next URL or a cached destination has failed, returned 402, or timed out. It also documents optional wallet-backed routing and bidding actions for outbid.sh.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends outbound requests to outbid.sh and then routes to dynamic destination URLs.

Mitigation: Install it only in environments where those outbound requests and dynamic destinations are allowed, and review the returned URL before forwarding requests.

Risk: Wallet-backed routing and bidding can create non-refundable USDC payment actions.

Mitigation: Require explicit user approval and spending limits before using /next or /bid.

Risk: Forwarded headers may be copied to the selected destination.

Mitigation: Forward only the headers returned for the route and avoid adding unrelated credentials or sensitive headers.

## Reference(s):

- [Outbid homepage](https://outbid.sh)
- [Outbid canonical skill file](https://outbid.sh/skill.md)
- [ClawHub skill listing](https://clawhub.ai/agent-default/skills/outbid)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls]

**Output Format:** [Markdown with inline bash code blocks and endpoint instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes outbound HTTP requests to outbid.sh and optional wallet or bidding actions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
