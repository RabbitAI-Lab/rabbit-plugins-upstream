## Description:

Data Analysis uses CellCog to analyze and visualize uploaded datasets, including data cleaning, exploratory analysis, statistical reports, machine learning model evaluation, charts, dashboards, and Python-backed workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to upload structured datasets to CellCog for profiling, cleaning, transformation, statistical analysis, visualization, dashboard generation, reporting, and machine learning evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded datasets may contain personal, regulated, proprietary, credential-bearing, or otherwise sensitive information and may be processed by CellCog.

Mitigation: Use redacted or synthetic data unless external processing is approved and CellCog privacy, retention, and access controls have been verified.

Risk: Generated analyses, statistical conclusions, charts, or recommendations may be incorrect if the data quality, assumptions, or prompt are insufficient.

Mitigation: Review methodology, source data, transformations, statistical assumptions, and generated outputs before relying on results for business or research decisions.

Risk: The skill requires a CELLCOG_API_KEY, which could expose access if placed in prompts, uploaded files, or shared logs.

Mitigation: Provide the API key through environment or secret management and avoid including credentials in datasets or prompts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/data-analysis-cellcog)
- [CellCog Homepage](https://cellcog.ai)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples and produced analysis artifacts such as HTML dashboards, PDF reports, CSV/XLSX files, charts, and Markdown summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, CELLCOG_API_KEY, and the cellcog dependency; uploaded datasets may be processed by CellCog.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
