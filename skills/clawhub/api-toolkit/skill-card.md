## Description: <br>
Api Toolkit is a professional API testing and debugging skill for regression suites, local mocks, load testing, OpenAPI contract checks, error lookup, and team collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, SREs, and API teams use this skill to generate and run API regression tests, mocks, load tests, and contract checks across development, CI, and release readiness workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Load tests can disrupt services or trigger third-party rate limits when aimed at production or unapproved targets. <br>
Mitigation: Run load tests only against owned or explicitly authorized systems, preferably staging environments, with agreed concurrency, duration, and rollback limits. <br>
Risk: Mock recording and replay workflows can capture real API traffic, credentials, tokens, or personal data. <br>
Mitigation: Enable redaction, store recordings outside source control, and verify generated recordings before sharing them with a team workspace. <br>
Risk: Agent-driven API testing commands can execute network requests and create files based on user-provided specs or examples. <br>
Mitigation: Review generated commands, OpenAPI specs, target URLs, and output paths before execution, and keep secrets in environment variables or approved credential stores. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-toolkit) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, YAML, and bash examples plus generated API test, mock, contract-check, and load-test artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run local CLI workflows that create reports, recordings, mock responses, or CI configuration; review targets and credentials before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
