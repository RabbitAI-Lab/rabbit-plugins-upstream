## Description: <br>
Monthly content performance and output-analysis skill that aggregates published content, the content calendar, channel-effect data, product-line coverage, and knowledge-base health, then outputs a monthly report and next-cycle optimization suggestions without auto-modifying the schedule or triggering writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content marketing teams use this skill to review monthly published output, schedule variance, channel performance, product-line coverage, and knowledge-base health. It produces a sourced monthly report with concrete findings and next-cycle recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-specified content calendar, published-content, channel metrics, product map, and knowledge-base files, and writes a report under reports/. <br>
Mitigation: Confirm the intended input paths and report destination before installation or execution. <br>
Risk: Product-line results may be less reliable when the product map is missing because the fallback allows title-based inference. <br>
Mitigation: Provide the product-line map where possible and preserve boundary notes when fallback inference is used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-performance-analyst) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, guidance] <br>
**Output Format:** [Markdown report saved to reports/YYYY-MM-monthly-report.md] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Marks missing effect data as DATA_MISSING and requires findings to cite a date, file, or data point.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
