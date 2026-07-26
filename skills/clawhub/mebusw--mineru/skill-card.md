## Description: <br>
Mineru Extract helps agents use MinerU APIs to extract key information from PDF and image documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mebusw](https://clawhub.ai/user/mebusw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route PDF, image, and supported office-document parsing requests through MinerU APIs and return the extracted content, typically as Markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents or URLs selected by the user may be sent to MinerU or related remote APIs. <br>
Mitigation: Process only approved documents, and avoid confidential, regulated, or internal-only files unless authorized. <br>
Risk: Generated output files may be created in the current working directory. <br>
Mitigation: Run the skill from a workspace where new files will not overwrite important content, and review outputs before relying on them. <br>
Risk: The Precision Parse API uses a MinerU API key stored through local environment configuration. <br>
Mitigation: Keep the API key out of version control and rotate it if it is exposed or expired. <br>


## Reference(s): <br>
- [MinerU API documentation](https://mineru.net/apiManage/docs) <br>
- [Source repository](https://github.com/mebusw/mineru) <br>
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/mineru) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, files] <br>
**Output Format:** [Markdown guidance with shell command and configuration examples; parsed document results are returned as Markdown files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written in the user's current working directory; Precision Parse results are consolidated from full.md files when available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
