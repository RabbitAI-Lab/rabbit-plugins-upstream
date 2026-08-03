## Description: <br>
WebSculpt bootstraps browser automation with a reusable command library by installing or repairing its CLI and lifecycle skills for external information gathering, scraping, API calls, and browser tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bqw1013](https://clawhub.ai/user/bqw1013) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to set up WebSculpt, then route browser automation and repeatable web information workflows into the appropriate WebSculpt lifecycle skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags persistent global installs that can affect future agent sessions. <br>
Mitigation: Prefer project-local installation when possible and ask the agent to report exact install paths and package versions before making changes. <br>
Risk: The skill can add global npm tooling and lifecycle skills under home-directory agent skill folders. <br>
Mitigation: Review requested install scope before execution and verify WebSculpt status after installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bqw1013/skills/websculpt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install global npm tooling and persistent lifecycle skills when the environment is not already configured.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
