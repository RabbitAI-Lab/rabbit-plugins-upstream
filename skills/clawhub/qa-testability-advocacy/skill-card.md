## Description: <br>
Chinese-language QA guidance skill for evaluating software testability across controllability, observability, isolation, automation, and diagnosability, then producing assessment reports, improvement suggestions, refactoring guidance, and best practices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, test leads, and development teams use this skill when features are difficult to test or architecture reviews need testability advocacy. It helps assess testability gaps and turn them into traceable improvement suggestions and implementation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest cleanup of test data as part of improving data-layer testability. <br>
Mitigation: Review cleanup suggestions before applying them and limit any cleanup to non-critical test data. <br>
Risk: Guidance may omit some testability issues for complex systems. <br>
Mitigation: Supplement the assessment with code review when gaps are suspected, then rerun the improvement planning step. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured assessment sections and traceable suggestion IDs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a testability assessment, improvement suggestions, refactoring guidance, and best-practice recommendations.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
