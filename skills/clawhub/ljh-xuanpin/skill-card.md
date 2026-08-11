## Description:

ljh-xuanpin is an e-commerce product selection advisor that checks a candidate product through five evidence-based steps and returns a pursue, do-not-pursue, or collect-more-data verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and product teams use this skill to evaluate whether a candidate product is worth pursuing by checking category opportunity, market size, competitor weaknesses, negative-review pain points, and SKU fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and write local business-analysis dossier and report files.

Mitigation: Review the target workspace before use, keep backups of important local files, and install only if local file persistence is acceptable.

Risk: The workflow can involve sensitive competitor, customer, or product-planning data.

Mitigation: Provide only data the user is authorized to share and redact confidential customer or competitor information before use.

Risk: Broad natural-language triggers may activate the skill outside the intended e-commerce product-selection workflow.

Mitigation: Prefer explicit /ljh-xuanpin invocation and confirm the task is product-selection analysis before following the workflow.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown product-selection assessment report with tables and optional local dossier or report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for product, competitor, sales or GMV, content, review, and SKU inputs before producing a verdict.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
