## Description:

Archive Zoom cloud recordings, read stored meeting transcripts and summaries, or manage a Zoom meeting through zm. Use for Zoom CLI workflows, not joining calls or operating the desktop video client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Zoom users and their agents use this skill to search and archive recorded meetings, read cited transcript evidence, prepare for scheduled series, and manage meetings through the Zoom CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote embedding search can send transcript passages to an external AI service, beyond the current search filters.

Mitigation: Use a local model or offline mode when transcript passages should not leave the environment.

Risk: Meeting changes made through MCP may run without an interactive confirmation prompt.

Mitigation: Require explicit user approval for meeting changes and review the target profile and action before applying them.

Risk: The bundled skill instructions do not assess the external Zoom CLI implementation.

Mitigation: Review the CLI's permissions and behavior before granting it access to accounts or communications sources.

## Reference(s):

- [Zoom Cli release on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-zoom)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance, Configuration]

**Output Format:** [Markdown guidance and CLI command examples, with structured JSON results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves evidence references and coverage details when available]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
