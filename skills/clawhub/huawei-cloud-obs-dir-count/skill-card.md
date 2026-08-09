## Description: <br>
Counts immediate or recursive directories in a Huawei Cloud OBS bucket or prefix and returns the numeric count without modifying OBS resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and storage administrators use this skill to inventory or verify the directory structure of Huawei Cloud OBS buckets and prefixes. It is suited for read-only capacity review, migration planning, structure checks, and compliance auditing where only folder counts are needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs OBS listing access and can expose bucket structure through directory counts. <br>
Mitigation: Grant only read-only OBS listing permissions, preferably scoped to the required bucket or prefix, and review whether directory-count results are appropriate to share. <br>
Risk: Huawei AK/SK credentials may be mishandled during CLI or obsutil setup. <br>
Mitigation: Configure credentials only in the user's own terminal, never paste secrets into chat, and account for obsutil storing credentials in the user's home configuration. <br>
Risk: The workflow invokes local shell commands and depends on hcloud, obsutil, and optional Huawei Cloud SDK behavior. <br>
Mitigation: Review commands before execution, verify the tools are installed from expected sources, and use the bundled verification method before relying on results. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text integer for successful counts, with concise Markdown guidance for setup, command selection, or error handling.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only OBS listing workflow; successful script output is a single non-negative integer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
