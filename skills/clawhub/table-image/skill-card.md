## Description: <br>
Generate images from tables for better readability in messaging apps like Telegram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joargp](https://clawhub.ai/user/joargp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to turn markdown tables into PNG images for messaging platforms that do not render markdown tables well. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on installing and running the external tablesnap Go command-line tool, including install guidance that uses @latest. <br>
Mitigation: Review the tablesnap project before use and pin a trusted version or release in stricter environments. <br>
Risk: Unsupported emoji can render as placeholder boxes until the full emoji set is installed. <br>
Mitigation: Install the optional emoji set with tablesnap when full emoji rendering is required, or avoid unsupported emoji in generated tables. <br>


## Reference(s): <br>
- [Table Image on ClawHub](https://clawhub.ai/joargp/skills/table-image) <br>
- [tablesnap repository](https://github.com/joargp/tablesnap) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and MEDIA file references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces PNG table images through the external tablesnap CLI; supports theme, font size, padding, and optional emoji installation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
