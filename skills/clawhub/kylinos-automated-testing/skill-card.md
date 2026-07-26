## Description: <br>
Guides an agent through GUI compatibility testing for Kylin V11 desktop applications without depending on a specific automation toolchain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cyanogenic](https://clawhub.ai/user/cyanogenic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to plan and execute installation, launch, GUI function, uninstall, and reporting workflows for Kylin V11 desktop software compatibility testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan notes sensitive maintainer, observability, and external-service workflow capabilities. <br>
Mitigation: Install only when those workflows are intended and review configured tokens, connected accounts, and service access before use. <br>
Risk: The skill guides agents to install and uninstall packages and control desktop windows during testing. <br>
Mitigation: Run tests in an isolated desktop session or disposable test environment and scope package, process, and file operations to the target application. <br>
Risk: GUI judgments may be wrong when screenshots, OCR, or LLM observations conflict. <br>
Mitigation: Use the skill's fact-conflict checks, screenshot evidence, logs, and explicit uncertainty states before attributing failures to compatibility issues. <br>


## Reference(s): <br>
- [Kylinos Automated Testing on ClawHub](https://clawhub.ai/cyanogenic/skills/kylinos-automated-testing) <br>
- [cyanogenic publisher profile](https://clawhub.ai/user/cyanogenic) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text, markdown] <br>
**Output Format:** [Markdown guidance with structured testing report expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces procedural testing guidance and report content; no toolchain-specific output files are required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
