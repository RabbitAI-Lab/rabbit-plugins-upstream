## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through zm. Use for Zoom CLI workflows, not joining calls or operating the desktop video client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External Zoom users and developers use this skill to search and read stored meeting transcripts, archive recordings, prepare cited meeting context, and manage Zoom meetings through zm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote embedding providers may receive transcript passages.

Mitigation: Use a local embedding model or a provider approved to receive the transcripts.

Risk: Broader searches and meeting changes can expose additional information or alter Zoom meetings.

Mitigation: Review broader searches and proposed changes before authorizing them.

Risk: MCP changes at the ask level do not display a server confirmation prompt.

Mitigation: Configure client-side approvals or read-only permissions for MCP.

## Reference(s):

- [Zoom CLI on ClawHub](https://clawhub.ai/wirecat/skills/zoom-cli)
- [wirecat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance with shell command examples; retrieved meeting evidence and recording archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on the selected Zoom profile, configured sources, and available stored or remote meeting data.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
