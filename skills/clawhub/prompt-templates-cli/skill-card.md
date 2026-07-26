## Description: <br>
Render parameterized prompt templates from a catalog with {{var}} variables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt engineers, and agent platform teams use this skill to manage reusable prompt templates, render them with variables, and validate template inputs before agent use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented curl install path fetches executable Python from GitHub. <br>
Mitigation: Review the fetched file or pin a trusted artifact before running it. <br>
Risk: Template catalog content is rendered and printed exactly as supplied. <br>
Mitigation: Use trusted catalog JSON files and review rendered prompt text before using it in an agent workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/prompt-templates-cli) <br>
- [Project GitHub Repository](https://github.com/itsPremkumar/prompt-templates-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and rendered prompt text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Rendered prompts are printed as supplied by the selected template catalog.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
