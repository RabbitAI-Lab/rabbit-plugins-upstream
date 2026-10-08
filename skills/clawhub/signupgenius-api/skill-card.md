## Description:

Guides agents in using curl to access SignUpGenius sign-ups, groups, and RSVPs without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use shell commands to read authorized SignUpGenius data and, with human confirmation, manage group membership or sign-up responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anonymous participant lookup may reveal details hidden in the normal public view.

Mitigation: Access only sign-ups and participant information you are authorized to use; do not bypass intended privacy settings.

Risk: Login credentials and session tokens may leak through shell history, logs, or temporary files.

Mitigation: Keep secrets out of history and logs, and protect or delete temporary cookie and header files.

Risk: Write commands can add members or change RSVPs and slot claims.

Mitigation: Require explicit human confirmation before adding members, submitting RSVPs, claiming slots, or withdrawing entries.

## Reference(s):

- [SignUpGenius API skill on ClawHub](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [SignUpGenius session-mode endpoint reference](artifact/references/sug-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve account, group, sign-up, and participant information or submit changes.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
