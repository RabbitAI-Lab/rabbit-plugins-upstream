## Description:

Generates brokerage-style equity research reports in PDF or Word format from financial data, DCF valuation output, comparable-company analysis, and optional charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Financial analysts and agent workflows use this skill to turn prepared financial-data, DCF, and comps JSON outputs into formatted Chinese equity research reports with valuation sections, business summaries, risk factors, and an automated buy, hold, or sell rating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain inaccurate financial inputs, valuation assumptions, hardcoded company profile details, or automated investment ratings.

Mitigation: Review the input data, assumptions, company profile fields, and buy, hold, or sell rating before relying on the report for any investment decision.

Risk: Missing DCF, comps, or financial-data JSON inputs can leave report sections blank or incomplete.

Mitigation: Provide all required JSON inputs and review the generated PDF or DOCX for completeness before distribution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PDF or DOCX research report files generated from JSON analysis inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DCF, comps, and financial-data JSON inputs for complete reports; optional chart directory and output path are supported.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
