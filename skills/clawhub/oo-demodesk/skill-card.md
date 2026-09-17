## Description:

Demodesk (demodesk.com). Use this skill for ANY Demodesk request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to read Demodesk data through an OOMOL-connected account, including users, recordings, transcripts, scorecards, and AI-generated recording summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands piped directly to a shell.

Mitigation: Install the oo CLI only after independently verifying the installer source, or use a signed or package-managed installation path where available.

Risk: Demodesk recording and transcript data is accessed through OOMOL's connector.

Mitigation: Install only when the user trusts OOMOL and is comfortable routing Demodesk data through that connector.

## Reference(s):

- [Demodesk homepage](https://demodesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-demodesk)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
