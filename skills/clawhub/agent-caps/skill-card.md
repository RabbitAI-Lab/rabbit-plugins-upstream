## Description: <br>
Define, validate, and audit agent capability manifests for safe skill installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and security reviewers use this skill to validate, scaffold, and cross-check agent capability manifests before publishing or installing agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scaffold workflow can create or overwrite agent-manifest.json in the directory supplied by the user. <br>
Mitigation: Run scaffold only in the intended project directory and review any existing agent-manifest.json before replacing it. <br>
Risk: Manifest validation depends on the JSON files supplied by the user. <br>
Mitigation: Review manifest files from untrusted sources before running validation or dependency checks. <br>
Risk: Executing a freshly downloaded remote script can run code the user has not inspected. <br>
Mitigation: Download the tool from a trusted source, inspect the file, and avoid piping remote downloads directly into execution. <br>


## Reference(s): <br>
- [Agent Caps on ClawHub](https://clawhub.ai/itspremkumar/skills/agent-caps) <br>
- [Agent Caps GitHub repository](https://github.com/itsPremkumar/agent-caps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or overwrite agent-manifest.json when scaffolding a target directory.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
