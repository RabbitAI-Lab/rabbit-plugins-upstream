## Description:

Evite API helps agents query and act on Evite events, guest lists, RSVPs, and messages from a shell using curl, authenticated cookies, and Evite internal endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Evite event data and prepare curl-based actions for RSVPs, guest lists, messages, templates, photos, and invitation lifecycle operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an agent to handle an Evite password or authenticated session cookie.

Mitigation: Use a restricted cookie jar, avoid logging credentials or guest data, and install only when this credential access is acceptable.

Risk: Write commands can change RSVPs, send messages, broadcast emails, send invitations, cancel events, or reinstate events without a built-in confirmation step.

Mitigation: Keep usage read-only by default, explicitly approve each write, verify event and guest IDs before execution, and test sends or broadcasts only on throwaway events.

Risk: Some write request bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed endpoints as less certain, inspect generated payloads before execution, and verify behavior on non-production or disposable events first.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Evite cookies and may include commands that read or mutate real Evite events.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
