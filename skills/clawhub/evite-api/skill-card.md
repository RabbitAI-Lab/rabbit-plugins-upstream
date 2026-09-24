## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell with curl and a cookie jar using Evite session cookies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Evite events, guest lists, RSVPs, messages, and templates, and to run authenticated Evite actions from shell workflows without the evite-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Evite credentials and a live session cookie, which can expose the account if logged, shared, or stored insecurely.

Mitigation: Use a secret manager for credentials, restrict the cookie jar file permissions, avoid logging raw cookies or guest-list responses, and delete the jar when the session is no longer needed.

Risk: Write actions can mutate real Evite data, including RSVPs, guest lists, broadcasts, invitations, photo uploads, and event cancellations.

Mitigation: Require explicit human approval before every write action and test sends or broadcasts only against a throwaway event with non-deliverable test guests.

Risk: Some write bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed request shapes as lower confidence and validate them on a low-impact event before using them with real guests.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl and jq shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API request recipes that read or mutate Evite account data.]

## Skill Version(s):

1.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
