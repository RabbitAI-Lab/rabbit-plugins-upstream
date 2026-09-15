## Description:

Provides read-only Otter.ai access through the OOMOL otter_ai connector and oo CLI for listing conversations, channels, members, workspace details, and temporary audio URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents with an OOMOL-connected Otter.ai account use this skill to inspect Otter.ai conversations, temporary audio links, workspace details, channels, and channel members through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that could execute unverified code in a shell.

Mitigation: Review the installer path before installing, prefer OOMOL signed or package-manager installation instructions, and avoid piping remote scripts directly into a shell.

Risk: Connected Otter.ai transcripts, temporary audio links, workspace data, channel data, and member data may be routed through OOMOL's connector.

Mitigation: Connect only accounts whose Otter.ai data is acceptable to route through the OOMOL connector, and avoid connecting sensitive workspaces unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-otter-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Otter.ai homepage](https://otter.ai)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and PowerShell command examples; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-oriented oo connector actions; temporary audio URL output may expire.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
