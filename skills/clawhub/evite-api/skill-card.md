## Description:

This skill helps agents query and act on Evite events, guest lists, RSVPs, messages, invitations, and event media from a shell using curl with an authenticated cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused users can use this skill to inspect Evite event data and prepare curl commands for authenticated reads and writes without running the Evite MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform direct Evite account writes, including RSVPs, guest edits, broadcasts, invitation sends, uploads, cancellations, and reinstatements.

Mitigation: Require explicit user confirmation before any write action and test high-impact actions against a throwaway event before using real guests or events.

Risk: The workflow uses stored Evite session cookies and CSRF tokens that could grant access if exposed.

Mitigation: Run only from a trusted environment, restrict the cookie jar permissions, keep it private, and avoid sharing logs that include cookies or tokens.

Risk: Some write request bodies are described as assumed rather than fully verified.

Mitigation: Treat assumed write bodies as lower confidence, verify behavior with a non-production event, and avoid retrying uncertain writes blindly.

Risk: The skill relies on Evite internal endpoints rather than a public API.

Mitigation: Re-check endpoint behavior before critical use and stop if authentication, CSRF rotation, or response shapes differ from the reference.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [Evite website](https://www.evite.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command blocks, curl examples, and JSON request or response notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Evite API calls that require a private cookie jar and fresh CSRF token handling.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
