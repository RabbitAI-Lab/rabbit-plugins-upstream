## Description:

Conducts deep small-molecule drug target research, including druggability, competitive landscape, patent posture, indications, structural biology, assay availability, safety, and strategic recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drtony1](https://clawhub.ai/user/drtony1)

### License/Terms of Use:

MIT-0

## Use Case:

Drug discovery researchers, analysts, and developers use this skill to assemble target research reports for small-molecule programs. It guides collection and synthesis of target biology, structures, assays, indications, competition, patents, safety, literature, and project strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated target research reports may contain proprietary strategy, confidential context, or sensitive competitive analysis.

Mitigation: Run the skill only in approved workspaces and review reports before sharing or uploading them.

Risk: The workflow uploads generated reports to a configured Google Drive remote without explicit confirmation.

Mitigation: Use a trusted, access-controlled rclone remote or change the workflow so cloud upload is opt-in and local-only output is the default.

## Reference(s):

- [Skill workflow](artifact/SKILL.md)
- [Analysis prompts](artifact/references/analysis-prompts.md)
- [Data sources](artifact/references/data-sources.md)
- [Report template](artifact/references/report-template.md)
- [UniProt](https://www.uniprot.org/)
- [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/)
- [RCSB Protein Data Bank](https://www.rcsb.org/)
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)
- [ClinicalTrials.gov](https://clinicaltrials.gov/)
- [KEGG Pathway](https://www.kegg.jp/kegg/pathway.html)
- [Reactome](https://reactome.org/)
- [ClawHub skill page](https://clawhub.ai/drtony1/skills/target-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [HTML report plus structured text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow saves a local HTML report and includes a Google Drive upload command when configured.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
