## Description:

Guides agents to query Evite events, guest lists, RSVPs, and messages and perform account actions using shell commands and an authenticated session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Evite account holders use this skill to inspect event details and guest responses or manage invitations, messages, and events from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and session cookies grant access to guest contact details.

Mitigation: Restrict access to credentials and cookie files, and avoid logging or retaining guest information unless necessary.

Risk: Account actions can change guest lists, RSVPs, and events or send invitations and broadcasts without a built-in confirmation step.

Mitigation: Require explicit user confirmation before any write, send, cancellation, guest-list change, or photo upload; test sends only with a throwaway event.

Risk: Some message and invitation request bodies are unverified, and event creation may appear to fail after creating a draft.

Mitigation: Verify the intended action and its result before repeating a request; check draft events before retrying a failed creation.

## Reference(s):

- [Evite endpoint reference](artifact/references/endpoints.md)
- [Evite API skill on ClawHub](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Evite account credentials and session cookies; commands may act on live events.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
