## Description:

evite-api helps agents query and act on Evite events, guest lists, RSVPs, and messages from a shell using curl, session cookies, and Evite's internal web endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to inspect Evite event data and generate authenticated curl workflows for reads and writes when they do not want to run the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated POST, PUT, PATCH, or DELETE commands can change live Evite events, guest lists, RSVPs, messages, invitations, uploads, or cancellations.

Mitigation: Before execution, verify event IDs, guest IDs, recipient counts, message bodies, HTTP methods, request bodies, and file paths; test write workflows against a throwaway event first.

Risk: The cookie jar and account credentials provide live access to an Evite account.

Mitigation: Store credentials carefully, restrict the cookie jar permissions, keep it out of shared locations, and delete the jar when finished.

Risk: Some write request bodies are documented as assumed rather than fully verified.

Mitigation: Treat guest messaging and invitation-send bodies as less certain, validate them on non-production or throwaway events, and avoid real recipients until the behavior is confirmed.

Risk: A create-event request can appear to fail after creating a draft, which may lead to duplicate events if retried blindly.

Mitigation: After an ambiguous create response, re-list draft events and confirm whether the event already exists before retrying.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl workflows that may perform authenticated reads and live writes against an Evite account.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
