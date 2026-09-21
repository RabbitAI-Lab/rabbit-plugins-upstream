## Description:

Encodian helps agents inspect live Encodian action schemas and run PDF-focused Encodian operations through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Encodian connector schemas and run Encodian PDF compression, extraction, text-layer, encryption, and unlock actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to run remote shell installation commands for the oo CLI during first-time setup.

Mitigation: Review the installer first or install the oo CLI manually before allowing the agent to use Encodian actions.

Risk: Encodian actions process user-provided PDF documents through an OOMOL-brokered connected account.

Mitigation: Use the skill only when that document handling model is acceptable for the data involved.

Risk: PDF unlock, extraction, encryption, compression, and other transformations can alter documents or expose their contents.

Mitigation: Require explicit user approval for the exact payload and expected effect before running transformation actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-encodian)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Encodian homepage](https://www.encodian.com)
- [OOMOL Encodian connection settings](https://console.oomol.com/app-connections?provider=encodian)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector responses are JSON and may include base64 PDF file content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Encodian account; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
