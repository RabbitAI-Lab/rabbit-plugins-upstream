## Description: <br>
Writes local text, code, configuration, Word, and Excel files in enterprise policy environments with explicit encoding handling; it does not provide file encryption or access-control bypass. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endcy](https://clawhub.ai/user/endcy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and enterprise users use this skill to create or append local files they are already authorized to access, especially when they need predictable text encoding or simple Office document output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes to local paths and can overwrite or append files. <br>
Mitigation: Review the destination path and content before execution, and run the agent with least-privilege filesystem access. <br>
Risk: The public name may imply encryption, but the artifact states that the skill does not encrypt files or bypass access controls. <br>
Mitigation: Use operating-system or dedicated encryption tools when encryption is required, and treat this skill only as a file writer. <br>
Risk: The security summary reports no evidenced malicious or suspicious behavior, but notes that package files could not be inspected in that scan run. <br>
Mitigation: Review the skill permissions and installation instructions before installing, especially for broad local file access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/endcy/skills/encrypted-file-writer) <br>
- [README](artifact/README.md) <br>
- [Verification report](artifact/VERIFICATION_REPORT.md) <br>
- [SkillSpector fix report](artifact/FIX_REPORT_v1.2.0.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Local files plus console status lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports overwrite and append modes, stdin content, configurable text encoding, and minimal .docx/.xlsx generation.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
