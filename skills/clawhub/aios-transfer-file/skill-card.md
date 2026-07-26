## Description: <br>
Transfers OpenClaw and AIOS files through an S3-compatible SDK by downloading file_input:// URIs into the current senderId workspace and uploading current senderId files as file_output:// URIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kadbbz](https://clawhub.ai/user/kadbbz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill in controlled OpenClaw or AIOS environments to receive user-provided files into a senderId-isolated workspace and return generated files through S3-compatible storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: S3 credentials or bucket permissions could expose more files than intended. <br>
Mitigation: Use least-privilege credentials and restrict the configured inbox and outbox buckets to the intended AIOS/OpenClaw deployment. <br>
Risk: A missing or incorrect senderId could mix files across workspace sessions. <br>
Mitigation: Require an explicit senderId for every transfer and stop when the current senderId cannot be confirmed. <br>
Risk: Uploads send current-session local files to external S3-compatible storage. <br>
Mitigation: Upload only files inside the current senderId directory and return a file_output:// URI only after the SDK upload succeeds. <br>
Risk: Missing runtime dependencies or S3 environment variables can cause failed transfers. <br>
Mitigation: Install the skill's local Node.js dependencies and verify required AIOS_S3_* configuration before running the transfer script. <br>


## Reference(s): <br>
- [Artifact README](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/kadbbz/skills/aios-transfer-file) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; transfer script emits JSON results or file_output:// URI strings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires senderId workspace isolation, S3-compatible environment variables, and local Node.js dependencies.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
