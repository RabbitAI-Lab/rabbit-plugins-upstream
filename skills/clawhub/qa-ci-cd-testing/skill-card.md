## Description: <br>
Provides CI/CD testing guidance for layered pipeline quality gates, tool integration strategy, and fast feedback across commit checks, unit tests, API tests, UI tests, and regression tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and DevOps teams use this skill to design CI/CD test stages, define quality gates, and tune feedback loops for reliable automated delivery pipelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pipeline or deployment suggestions may affect production delivery if applied without review. <br>
Mitigation: Review generated CI/CD, deployment, rollback, and quality-gate recommendations before use, especially in production environments. <br>
Risk: The skill can propose CI/CD testing strategy but does not execute pipelines or validate environment-specific behavior. <br>
Mitigation: Keep execution under explicit user control and validate changes in an authorized workspace or staging environment first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ci-cd-testing) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown with structured pipeline design, test-stage, quality-gate, and feedback-loop sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pipeline recommendations include traceability IDs and should be reviewed before applying to production CI/CD systems.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
