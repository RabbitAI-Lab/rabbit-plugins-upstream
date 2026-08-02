## Description: <br>
WebSculpt bootstraps and repairs a browser automation CLI and lifecycle skill set for acquiring web information and turning repeated browser workflows into reusable commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bqw1013](https://clawhub.ai/user/bqw1013) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to install, verify, update, or repair WebSculpt before using browser automation for information acquisition, scraping, API work, or reusable command-library workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can install global tools and persistent agent skills across the user's home directory without a separate approval step. <br>
Mitigation: Confirm the install scope, npm packages, and target skill directories before running install commands; use a project-local install when global availability is not needed. <br>
Risk: Browser automation in logged-in sessions or on third-party sites can expose account data or perform actions as the user. <br>
Mitigation: Use least-privilege browser sessions, review target sites and actions before execution, and avoid sensitive accounts unless they are required for the task. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
