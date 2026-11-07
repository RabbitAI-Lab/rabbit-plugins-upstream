## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through the `zm` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Zoom users and their agents use this skill to find and review stored meeting evidence, archive recordings and transcripts, and manage meetings through the `zm` command line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands could use an unintended Zoom profile or access an unintended communications source.

Mitigation: Ask the user to select the profile and explicitly configure any additional accounts or folders; do not broaden the selected scope.

Risk: Remote embedding search sends transcript passages to the selected provider.

Mitigation: Enable remote embeddings only with the user's approval.

Risk: MCP writes can apply changes without an interactive question.

Mitigation: Require approval for MCP writes and restart MCP after revoking source access.

## Reference(s):

- [Zoom Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-zoom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Structured data]

**Output Format:** [Markdown with shell commands, meeting excerpts, source references, and structured CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be bounded or incomplete; retain source references and coverage details when reporting evidence.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
