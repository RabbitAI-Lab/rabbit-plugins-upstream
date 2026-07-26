## Description: <br>
Enables agents to drive a local Chrome browser with natural-language commands for navigation, element interaction, screenshots, and page data extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, students, freelancers, and individual automation users use this skill to simplify local Chrome browser tasks such as information collection, form interaction, page observation, screenshots, and structured extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can combine browser control with command-execution assistance on the user's machine. <br>
Mitigation: Install only when local browser automation and command execution are acceptable; review commands before execution and prefer a dedicated browser profile. <br>
Risk: Privacy and data-flow disclosures are inconsistent for callbacks, screenshots, extracted page text, and LLM processing. <br>
Mitigation: Avoid confidential pages or sensitive accounts until data flows are confirmed; avoid callback URLs and screenshots unless they are necessary for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/stagehand-browser-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON] <br>
**Output Format:** [Markdown guidance with bash examples and JSON result objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser screenshots, extracted page text, command status, result data, execution logs, and error details when automation commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
