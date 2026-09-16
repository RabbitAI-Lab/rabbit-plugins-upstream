## Description:

Population genetics of pre-aligned DNA sequences or multi-sample VCFs using selected DnaSP 6 methods for diversity, neutrality statistics, linkage disequilibrium, InDel polymorphism, divergence, MK, Ka/Ks and codon usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drdaviddelorenzo](https://clawhub.ai/user/drdaviddelorenzo)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers and analysts use this skill to run local population-genetics analyses on pre-aligned DNA sequences or supported multi-sample VCF files, then review generated reports, tables, plots and reproducibility artifacts. It is not intended for sequence alignment, phasing, unsupported significance tests or clinical interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied sequence, VCF, population and HKA input files may be copied into the output directory for reproducibility.

Mitigation: Choose an appropriate output location and keep generated outputs private when working with sensitive or identifiable genetic data.

Risk: Running analyses in a reused or shared output folder can expose prior artifacts or mix results.

Mitigation: Run the skill in a normal project sandbox with a fresh output folder for each analysis.

## Reference(s):

- [Server-resolved GitHub source import](https://github.com/drdaviddelorenzo/dnasp/tree/main/skills/dnasp)
- [Project homepage](https://github.com/drdaviddelorenzo/dnasp)
- [ClawHub skill page](https://clawhub.ai/drdaviddelorenzo/skills/dnasp)
- [DnaSP statistical reference](docs/index.md)
- [DnaSP 6 publication](https://doi.org/10.1093/molbev/msx248)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown reports with JSON summaries, TSV tables, optional PNG figures and reproducibility files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and may copy supplied sequence, VCF, population and HKA input files into the selected output directory for reproducibility.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; packaged skill frontmatter and changelog report 0.5.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
