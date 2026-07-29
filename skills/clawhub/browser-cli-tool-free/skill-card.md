## Description: <br>
This skill guides agents in using a Playwright-based browser CLI for page navigation, element interaction, screenshots, and page information extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users can use this skill to drive browser workflows such as site check-ins, form filling, screenshots, page snapshots, and lightweight information extraction through CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can submit forms, use credentials, capture sensitive pages, or create scheduled jobs beyond the user's intent. <br>
Mitigation: Require explicit review before form submission, credential use, sensitive screenshots, or scheduled automation, and keep activity limited to the requested browser task. <br>
Risk: The skill is loosely scoped and includes unrelated data-analysis trigger language. <br>
Mitigation: Invoke it only for CLI-driven browser automation, not for general data analysis or reporting tasks. <br>
Risk: Commands depend on a globally installed browser CLI, Node.js, Chromium, network access, and target website behavior. <br>
Mitigation: Confirm dependencies, site permissions, and command effects before running browser actions, especially on authenticated or sensitive pages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-cli-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to produce browser screenshots, page snapshots, extracted text, command logs, or structured JSON results when the referenced CLI is run.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
