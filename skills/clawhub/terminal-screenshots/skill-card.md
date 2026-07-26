## Description: <br>
Create terminal screenshots, animated GIFs, or videos using VHS scripts for documentation, demos, and reproducible CLI visuals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricardodantas](https://clawhub.ai/user/ricardodantas) <br>

### License/Terms of Use: <br>
GPL-3.0 <br>


## Use Case: <br>
Developers and technical writers use this skill to plan and generate reproducible terminal screenshots, animated GIFs, and videos for documentation, CLI demos, tutorials, and golden-file comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VHS tape files can run shell commands and write media files. <br>
Mitigation: Review every .tape file before execution and replace cleanup or write commands with clearly scoped disposable paths. <br>
Risk: Recorded terminal output may expose secrets or sensitive local context. <br>
Mitigation: Avoid recording terminals that display credentials, tokens, private paths, or other sensitive data, and inspect hidden setup sections before running. <br>
Risk: Hidden VHS sections can obscure setup, cleanup, or environment-changing commands from the final recording. <br>
Mitigation: Review Hide and Show blocks before execution and keep setup or cleanup commands minimal and explicit. <br>


## Reference(s): <br>
- [VHS GitHub](https://github.com/charmbracelet/vhs) <br>
- [VHS Themes](https://github.com/charmbracelet/vhs/blob/main/THEMES.md) <br>
- [VHS Example Tapes](https://github.com/charmbracelet/vhs/tree/main/examples) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with bash and VHS tape code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce VHS .tape scripts and commands that write PNG, GIF, MP4, WebM, or frame-sequence outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
