## Description: <br>
API test automation for REST and GraphQL APIs, including functional tests, performance tests, contract validation, mock services, and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to exercise REST and GraphQL APIs, validate contracts, run controlled performance tests, operate mock endpoints, and generate test reports for authorized API testing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API tests and load tests may send traffic to real services or targets the user is not authorized to test. <br>
Mitigation: Use the skill only for authorized API testing, prefer mock or staging endpoints, and keep concurrency conservative unless the target environment is approved for load testing. <br>
Risk: Authentication headers, cookies, request bodies, responses, and error output may appear in test reports or mock request logs. <br>
Mitigation: Use test credentials, avoid real production secrets in examples or configuration, and treat generated reports and mock logs as sensitive artifacts. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/kaiyuelv/api-test-automation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and shell examples, plus generated HTML, JSON, JUnit XML, and Allure-compatible reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform HTTP requests, start a local mock server, run pytest-based suites, and write report files.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
