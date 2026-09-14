## Description:

TinkerClaw OwnTracks Location is a self-hosted OwnTracks HTTP receiver and places CLI that lets an agent answer location and nearby-place queries from token-protected local location data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and individual users use this skill to connect OwnTracks phone pings to a local receiver so an agent can answer where-am-I questions, store named places, query nearby places, and inspect recent location history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recent location history is highly sensitive local data.

Mitigation: Keep the default loopback or private-network setup, retain the default pruning limits where possible, and use purge or revoke when the receiver is no longer needed.

Risk: Binding the receiver beyond loopback over plain HTTP can expose the token and coordinates on the network.

Mitigation: Avoid public exposure; use a private tunnel such as Tailscale or WireGuard, or place the receiver behind TLS and a firewall.

Risk: The fallback token file is a local secret if no OS keychain is available.

Mitigation: Prefer OS keychain storage, keep fallback files private, and revoke the token when access should end.

Risk: Reverse geocoding or sharing coordinates can disclose precise location to third-party services.

Mitigation: Report named places when sufficient and do not send precise coordinates to external services unless the user asks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/owntracks-location)
- [TinkerClaw project homepage](https://github.com/globalcaos/tinkerclaw)
- [OwnTracks HTTP mode reference](https://owntracks.org/booklet/features/http/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON endpoint responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local Node receiver, token-protected HTTP endpoints, and a local places CLI; no cloud service is contacted by the receiver.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
