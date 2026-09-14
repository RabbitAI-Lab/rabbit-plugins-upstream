## Description:

Query eventbrite.com from a shell: tickets and orders, organization events and attendees via the documented token API with curl, and public event discovery through the fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to compose read-only Eventbrite data queries from a shell, including token-authenticated account and organizer data plus browser-routed public event discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can use an authenticated Eventbrite session to access private account data.

Mitigation: Prefer token-based curl recipes for private data, use a dedicated browser profile or signed-out tab for public discovery when possible, and revoke the fpx/Transporter pairing after use.

Risk: The setup asks users to install and persistently pair a third-party browser bridge.

Mitigation: Install only after reviewing the bridge and extension permissions, and remove or unpair them when Eventbrite access is no longer needed.

## Reference(s):

- [Eventbrite documented API curl recipes](artifact/references/token-api.md)
- [Eventbrite discovery API fpx recipes](artifact/references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes for Eventbrite data retrieval; private account data requires an Eventbrite token or authenticated browser session.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
