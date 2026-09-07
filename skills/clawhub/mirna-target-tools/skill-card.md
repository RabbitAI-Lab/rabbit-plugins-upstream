## Description:

miRNA target prediction and annotation analysis for TargetScan/miRanda prediction, GO/KEGG enrichment, conservation analysis, and Cytoscape network construction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[destinqu](https://clawhub.ai/user/destinqu)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and bioinformatics analysts use this skill to run miRNA target prediction, merge high-confidence target results, annotate target genes, perform GO/KEGG enrichment, analyze sequence conservation, and prepare Cytoscape network files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional installer can make system-wide changes with sudo and install downloaded software from GitHub.

Mitigation: Review the installer before use, prefer manual dependency installation, or run installation in an isolated environment.

Risk: Gene lists and miRNA identifiers may be sent to MyGene.info or g:Profiler during annotation or enrichment workflows.

Mitigation: Treat input data as potentially shared with external services and use local or approved workflows for sensitive datasets.

Risk: Merged target results can be misread as high-confidence intersections without checking the merge evidence.

Mitigation: Verify merged outputs by checking the FoundInBoth column before relying on targets as high-confidence intersections.

## Reference(s):

- [Workflow Guide](references/workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/destinqu/skills/mirna-target-tools)
- [TargetScan](https://www.targetscan.org/)
- [TargetScan Data Downloads](https://www.targetscan.org/cgi-bin/targetscan/data_download.cgi)
- [miRanda 3.3a Source Archive](https://github.com/miRanda/miRanda/archive/refs/tags/3.3a.tar.gz)
- [g:Profiler API Endpoint](https://biit.cs.ut.ee/gprofiler/api/gost/profile/)
- [miRBase Mature FASTA](https://www.mirbase.org/download/mature.fa)
- [Cytoscape](https://cytoscape.org/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands plus generated TXT, TSV, PNG, SVG, and SIF analysis files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include target prediction tables, merged high-confidence target lists, gene annotation and enrichment tables, conservation summaries, sequence logo and alignment plots, and Cytoscape node/network files.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
