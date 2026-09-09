## Description:

Provides a self-hosted OwnTracks receiver and places CLI so an agent can answer location and nearby-place questions from locally stored, token-protected location data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who run OwnTracks can use this skill to let an agent answer where they are, record named places, query nearby places by distance, and inspect recent location history from their own machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles recent location history, which is highly sensitive personal data.

Mitigation: Install only when the user is comfortable granting the agent access to this data, keep retention caps enabled, and use --purge-data when the trail should be erased.

Risk: Binding the receiver beyond localhost over plain HTTP can expose the token and coordinates on the network.

Mitigation: Keep the listener on localhost or a private tunnel, and use TLS termination if it must be exposed beyond a private network.

Risk: A weak or mishandled receiver token could allow unauthorized reads or writes to location endpoints.

Mitigation: Use the generated token, store it in the OS keychain where possible, avoid putting it in service environment lines, and revoke or rotate it if exposure is suspected.

Risk: Running the optional service with elevated privileges can put location data and token access in the wrong user context.

Mitigation: Run the service only as the intended user, not as root or a system-wide service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/owntracks-location)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [Publisher profile](https://clawhub.ai/user/globalcaos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown with local CLI commands, HTTP request examples, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include location-derived answers, named-place summaries, and setup or privacy guidance for a token-protected local receiver.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
