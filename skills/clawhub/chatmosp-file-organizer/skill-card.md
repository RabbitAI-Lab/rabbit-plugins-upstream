## Description: <br>
File system manager for the chatMOSP system that creates MSR and KMC task directories, applies task naming rules, and keeps file operations inside the configured OUTPUT area. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators working with ChatMOSP use this skill after parameter confirmation to create standardized MSR and KMC output directories, validate task names, and prepare handoffs to companion simulation skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation inconsistencies may make KMC directory placement ambiguous between top-level OUTPUT tasks and subdirectories under an MSR task. <br>
Mitigation: Clarify whether the KMC workflow is direct or sequential, and confirm the parent MSR directory before creating or organizing KMC task files. <br>
Risk: Incorrect parameters or paths could organize files in an unintended location. <br>
Mitigation: Apply the documented whitelist, path traversal rejection, task-name validation, permission checks, and overwrite confirmation before any file operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanyangye/skills/chatmosp-file-organizer) <br>
- [Publisher profile](https://clawhub.ai/user/sanyangye) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with JSON examples, path layouts, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Restricts intended file operations to mosp-for-chatMOSP/OUTPUT/ and documents validation for task names, paths, permissions, and overwrite handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
