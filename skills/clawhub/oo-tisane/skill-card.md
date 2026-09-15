## Description:

Tisane (tisane.ai). Use this skill for ANY Tisane request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Tisane through an OOMOL-connected account for text analysis, language detection, translation, paraphrasing, text extraction, semantic similarity, and entity comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands that can execute code on the user's machine.

Mitigation: Review the oo CLI setup path before installing and prefer an official versioned package or verifiable installer instead of running pipe-to-shell commands directly.

Risk: Submitted text is processed through OOMOL's connector and Tisane.

Mitigation: Only connect an account intended for this use and submit text that is acceptable to process through those services.

## Reference(s):

- [Tisane homepage](https://tisane.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tisane)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
