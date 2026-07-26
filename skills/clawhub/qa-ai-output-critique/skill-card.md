## Description: <br>
QA AI Output Critique reviews AI-generated test cases across completeness, correctness, executability, risk coverage, formatting, traceability, consistency, and redundancy, producing scored quality reports and improvement suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers and developers use this skill after AI generates test cases to critique their quality before final delivery, identify coverage gaps, and guide iteration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: General QA phrases such as "check the output" may trigger the skill when the user intended a different kind of review. <br>
Mitigation: Confirm the intended review target before applying the skill to broad or ambiguous QA requests. <br>
Risk: The documentation mixes six- and eight-dimension review modes, which can make pass/fail thresholds inconsistent for strict quality gates. <br>
Mitigation: Standardize the selected review mode and scoring threshold before using the report as a gating result. <br>
Risk: Review suggestions may include merging, simplifying, or deleting low-value test cases. <br>
Mitigation: Treat these as non-persistent review proposals; back up source test data and require human confirmation before changing or deleting cases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ai-output-critique) <br>
- [Publisher profile](https://clawhub.ai/user/kokxi) <br>
- [Review dimensions](references/review-dimensions.md) <br>
- [Report templates](references/report-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown critique report with scores, issue tables, coverage gaps, quality score, and improvement suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May operate in complete or quick review mode depending on whether scenario trees, risk lists, and traceability data are provided.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
