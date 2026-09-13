## Description:

Generate a personalised nutrition report from your genetic data (23andMe, AncestryDNA, or VCF). Analyses 24 genes (28 SNPs) across 12 nutrient domains affecting nutrient metabolism, absorption, and food sensitivities. All processing is local — your genetic data never leaves your device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drdaviddelorenzo](https://clawhub.ai/user/drdaviddelorenzo)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to generate local nutrigenomics reports from consumer genetic files, including 23andMe, AncestryDNA, and VCF inputs. The report summarizes nutrient-domain risk scores, per-SNP calls, visualizations, and nutrition-oriented guidance for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports contain sensitive genetic-derived information and may be shared beyond the local environment.

Mitigation: Keep raw DNA files and reports out of shared or cloud-synced folders unless intended, review outputs before sharing, and delete the output directory when finished.

Risk: Dependency or supply-chain changes could affect a local analysis environment.

Mitigation: Install dependencies in an isolated environment and prefer reviewed lockfiles or hashes when stronger assurance is needed.

Risk: Nutrition guidance derived from genotype data can be mistaken for clinical advice.

Mitigation: Treat the report as decision support, review the output before acting on it, and involve qualified clinicians where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drdaviddelorenzo/skills/nutrigenomics)
- [Server-resolved GitHub provenance](https://github.com/drdaviddelorenzo/nutrigenomics/tree/main/skills/nutrigenomics)
- [Publisher profile](https://clawhub.ai/user/drdaviddelorenzo)
- [README](artifact/README.md)
- [OpenClaw metadata](artifact/openclaw.json)
- [Attribution and scientific references](artifact/ATTRIBUTION.md)
- [SNP panel](artifact/data/snp_panel.json)
- [GWAS Catalog](https://www.ebi.ac.uk/gwas/)
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown report with generated figure files and a reproducibility bundle]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written locally under the working directory and persist until manually deleted.]

## Skill Version(s):

0.3.11 (source: frontmatter, OpenClaw metadata, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
