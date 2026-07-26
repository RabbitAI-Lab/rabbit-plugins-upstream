## Description: <br>
Enterprise File Writer helps an agent write or append local text, code, configuration, log, and Office document files while documenting safety checks for sensitive paths and overwrites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill when they need to create, overwrite, or append authorized local files in enterprise environments, including text, source code, configuration, log, .docx, and .xlsx files. It is most appropriate when the target path and write intent are explicit and the user has permission to modify the file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can overwrite local files when directed. <br>
Mitigation: Review the target path before execution, warn before overwriting important files, and avoid using --force unless the user explicitly intends the write. <br>
Risk: Writing to sensitive paths, credential files, configuration files, or executable scripts can cause data loss, credential exposure, or system changes. <br>
Mitigation: Require explicit user confirmation for sensitive paths and scripts, verify that the content matches the user's request, and do not use the skill to bypass access controls. <br>
Risk: The server security guidance notes that GBK, GB2312, and Latin-1 encoding options are documented but not actually honored by the current code. <br>
Mitigation: Prefer UTF-8 writes and verify file contents after writing when a non-UTF-8 encoding is requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endcy/skills/enterprise-file-writer) <br>
- [Publisher profile](https://clawhub.ai/user/endcy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Local files plus command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can overwrite or append files and can create parent directories when invoked with an explicit target path.] <br>

## Skill Version(s): <br>
1.2.3 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
