## Description:

Guides agents in reading and managing Evite events, guest lists, RSVPs, and messages from the shell using authenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Evite account holders use this skill to check events and guest responses or manage invitations from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and live session cookies can expose Evite account access or private guest lists.

Mitigation: Avoid passwords in shell history and store cookie jars and guest lists only in restricted, non-shared locations.

Risk: Actions can change events or email real guests without a built-in confirmation step.

Mitigation: Require explicit confirmation before sends, broadcasts, cancellations, guest-list changes, or photo uploads; test with a throwaway event.

Risk: Two message and invitation request bodies are not verified, so these operations may fail or act unexpectedly.

Mitigation: Test unverified operations on a throwaway event before using them with real guests.

## Reference(s):

- [Evite endpoint reference](artifact/references/endpoints.md)
- [Evite API skill on ClawHub](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use an Evite account session; some actions change events or contact guests.]

## Skill Version(s):

1.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
