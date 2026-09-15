## Description:

Generate a personalised nutrition report from your genetic data (23andMe, AncestryDNA, or VCF). Analyses 24 genes (28 SNPs) across 12 nutrient domains affecting nutrient metabolism, absorption, and food sensitivities. All processing is local - your genetic data never leaves your device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drdaviddelorenzo](https://clawhub.ai/user/drdaviddelorenzo)

### License/Terms of Use:

MIT

## Use Case:

External users and health-focused developers use this skill to turn consumer genetic files into a local nutrition report with nutrient risk scores, per-SNP genotype calls, charts, and reproducibility notes. Results are educational and should be reviewed with a qualified healthcare professional before changing diet or supplements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive genetic data and writes a report containing per-SNP genotype calls.

Mitigation: Run it locally only in an environment appropriate for sensitive data, keep outputs under the user's control, and delete generated folders when they are no longer needed.

Risk: Generated reports can influence diet or supplement choices but are not diagnostic or medical advice.

Mitigation: Use the report as educational context and review findings with a qualified healthcare professional before making health changes.

Risk: Input filenames may identify a person in the generated report header.

Mitigation: Rename identifying genetic input files before analysis.

Risk: Python dependencies are version-bounded but not pinned with cryptographic hashes.

Mitigation: Install dependencies in an isolated environment from trusted package sources.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/drdaviddelorenzo/nutrigenomics/tree/main/skills/nutrigenomics)
- [ClawHub skill page](https://clawhub.ai/drdaviddelorenzo/skills/nutrigenomics)
- [Publisher profile](https://clawhub.ai/user/drdaviddelorenzo)
- [PubMed MEDLINE](https://pubmed.ncbi.nlm.nih.gov/)
- [GWAS Catalog](https://www.ebi.ac.uk/gwas/)
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)
- [OpenClaw](https://openclaw.ai)
- [SNP panel](data/snp_panel.json)
- [Attribution and citations](ATTRIBUTION.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with generated chart files and a JSON-compatible structured result for OpenClaw]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written locally under the working directory and persist until the user deletes them.]

## Skill Version(s):

0.3.12 (source: frontmatter, openclaw.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
