## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell with curl and a cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to automate authorized Evite account workflows from a shell, including reading event details and guest lists, managing RSVPs, sending messages or invitations, uploading photos, and changing event state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Evite account credentials and live session cookies.

Mitigation: Use only authorized accounts, store cookies in a private temporary jar with restrictive permissions, clean up the jar after use, and avoid leaving passwords in shell history or long-lived environment variables.

Risk: Write commands can change real events, RSVPs, guest lists, invitations, broadcasts, cancellations, and photo galleries.

Mitigation: Inspect each command before running it, require explicit human confirmation for writes, and test invitation sends or broadcasts only against throwaway events and non-deliverable test guests.

Risk: Guest lists, invite links, messages, and uploaded photos can contain sensitive personal data.

Mitigation: Limit use to events the operator is authorized to manage, minimize retained output, and treat saved command output and uploaded files as sensitive.

Risk: Two documented write request bodies are marked as assumed rather than fully verified.

Mitigation: Validate those operations on a disposable event before relying on them for a real event, and avoid blind retries after ambiguous responses.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [Evite](https://www.evite.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl, jq, environment variables, and a local cookie jar for authenticated Evite sessions.]

## Skill Version(s):

0.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
