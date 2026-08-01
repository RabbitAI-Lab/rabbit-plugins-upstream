## Description: <br>
帮助开发者编写、调试和优化自动化测试脚本，并生成测试代码、Page Object 代码、CI/CD 配置和测试报告指导。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and test engineers use this skill to create, debug, and improve automated tests for web, API, mobile, unit, integration, end-to-end, and performance testing workflows. It can produce framework-specific examples, Page Object models, CI/CD snippets, and testing best-practice guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated tests may log in, create records, control mobile emulators, change network state, install test dependencies, or run in CI. <br>
Mitigation: Use test accounts, test devices, and staging or local endpoints unless production exercise is explicitly intended and authorized. <br>
Risk: Generated test code or CI configuration may be incorrect for the target system or could exercise unintended systems if endpoints and credentials are not reviewed. <br>
Mitigation: Review generated code, configuration, endpoints, credentials, and permissions before execution, and constrain CI secrets and production access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shylamb-token/skills/auto-test-assistant) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/shylamb-token) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include runnable test scripts, Page Object models, CI/CD configuration, test report commands, and debugging guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
