## Description:

Klangio lets an agent operate Klangio through an OOMOL-connected account to create music-analysis jobs, check job status, and retrieve generated outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Klangio connector actions for beat tracking, chord recognition, source separation, strum recognition, transcription, status checks, and result downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage running mutable remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a pinned, verifiable release or trusted package manager before using the skill.

Risk: Several Klangio actions create jobs or otherwise change service state.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

## Reference(s):

- [Klangio homepage](https://klang.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-klangio)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector payloads; generated job outputs may be downloaded to OOMOL OSS transit storage.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
