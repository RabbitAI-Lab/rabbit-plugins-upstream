## Description: <br>
Qa Test Skills turns requirement documents into traceable, structured test cases through a 12-step QA workflow covering functional, boundary, combination, regression, review, and reporting activities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, testers, product teams, and developers use this skill to transform PRDs, uploaded files, URLs, or direct requirement descriptions into structured test cases, coverage reports, risk areas, and test reports. It is intended for workflows that need traceable requirements coverage and AI-assisted review of testing gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read referenced requirement files, linked subdocuments, directories, and user-provided URLs during QA analysis. <br>
Mitigation: Use explicit paths and avoid broad or sensitive directories unless those documents are intended for QA analysis. <br>
Risk: Generated test guidance can miss context or introduce misleading coverage conclusions if the supplied requirements are incomplete. <br>
Mitigation: Review the generated coverage report, risk areas, and validation report before using the test cases for release decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-skills) <br>
- [Enforcement rules](references/enforcement.md) <br>
- [Output format and checklist](references/format.md) <br>
- [Input routing rules](references/routing.md) <br>
- [Workflow detail](references/workflow-detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, CSV, Guidance] <br>
**Output Format:** [Markdown reports, CSV test cases, and structured JSON-style analysis blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are expected to include traceability identifiers for test cases, requirements, and scenarios.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
