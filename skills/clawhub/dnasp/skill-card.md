## Description:

Population genetics of pre-aligned DNA sequences or multi-sample VCFs using selected DnaSP 6 methods.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drdaviddelorenzo](https://clawhub.ai/user/drdaviddelorenzo)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers and analysts use this skill to run documented population-genetics analyses on pre-aligned DNA sequence files or supported multi-sample VCFs and receive reports, tables, summaries and reproducibility artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Output folders can include archived copies of input DNA or VCF files, checksums, command history and environment details.

Mitigation: Keep outputs local by default and share reproducibility bundles only when sharing those inputs and run details is intended.

Risk: Population-genetics statistics may be misread as clinical interpretation or unsupported significance claims.

Mitigation: Use the documented assumptions and only treat opt-in simulation P-values as significance assessments; do not use the skill for diagnosis or medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drdaviddelorenzo/skills/dnasp)
- [Homepage](https://github.com/drdaviddelorenzo/dnasp)
- [DnaSP statistical reference](docs/index.md)
- [Version history](docs/version_history.md)
- [DnaSP 6 methods paper](https://doi.org/10.1093/molbev/msx248)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, TSV tables, JSON summaries, optional PNG figures, shell commands and reproducibility files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3.10+; matplotlib is optional for figures.]

## Skill Version(s):

0.6.0 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
