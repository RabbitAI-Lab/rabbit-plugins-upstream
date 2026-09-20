## Description:

Extract content from PowerPoint (.pptx) presentations to Markdown using MinerU, including slide text, structure, formatting, page or slide selections, and quick or token-authenticated extraction paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mzlzyca](https://clawhub.ai/user/mzlzyca)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to extract readable Markdown from PowerPoint presentations for content review, documentation workflows, and automated processing. It is suited for local files or presentation URLs and can use MinerU's quick extraction path or token-authenticated full extraction for more complex slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Presentation content may be processed through the external MinerU CLI/API rather than entirely inside the local agent environment.

Mitigation: Use only with presentations approved for third-party MinerU/OpenDataLab processing, especially for confidential or regulated data.

Risk: Installing an unreviewed or unexpected mineru-open-api package version can change extraction behavior or supply-chain exposure.

Mitigation: Install from the expected MinerU/OpenDataLab package source and pin a reviewed version where environment controls require reproducibility.

## Reference(s):

- [MinerU homepage](https://mineru.net)
- [MinerU GitHub repository](https://github.com/opendatalab/MinerU)
- [MinerU API token management](https://mineru.net/apiManage/token)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown content with command examples and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses mineru-open-api; flash-extract can write Markdown to stdout or an output directory, while token-authenticated extraction supports richer slide content.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
