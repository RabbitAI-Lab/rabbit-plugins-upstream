## Description:

Glyphic (goairspeed.com). Use this skill for ANY Glyphic request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and read Glyphic data through an OOMOL-connected account, including calls, transcripts, summaries, media metadata, snippets, insights, playbooks, playbook versions, and call tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that could execute unverified code if run automatically.

Mitigation: Install the oo CLI through a separately trusted, verified process, then use this skill only after oo is already installed and connected.

Risk: Glyphic read actions can return call transcripts, summaries, media metadata, snippets, and insights.

Mitigation: Request only user-authorized Glyphic records and keep returned call data within the intended task context.

## Reference(s):

- [Glyphic homepage](https://www.goairspeed.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-glyphic)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Glyphic connector actions with live schema inspection before payload construction.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
