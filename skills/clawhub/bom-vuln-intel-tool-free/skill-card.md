## Description: <br>
Generates basic SBOMs and helps individual developers check npm and PyPI dependencies against public vulnerability data before dependency updates or release. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual developers and engineers use this skill to create a basic software bill of materials for a single npm or Python project, inspect package metadata, and check dependencies for known vulnerabilities before updating or shipping code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags mismatched activation instructions that mention database tasks even though the skill performs SBOM and dependency vulnerability work. <br>
Mitigation: Invoke the skill only for SBOM generation, package metadata lookup, or dependency vulnerability checks, and confirm the requested task matches that scope before running commands. <br>
Risk: Dependency names and versions may be sent to public OSV, npm, and PyPI services during checks. <br>
Mitigation: Use the skill only when sharing package metadata with those public services is acceptable, especially for private projects. <br>
Risk: The skill can run shell commands and write report files such as SBOM JSON outputs. <br>
Mitigation: Review generated commands and output filenames before execution to avoid unintended scans or overwriting existing files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bom-vuln-intel-tool-free) <br>
- [OSV API](https://api.osv.dev) <br>
- [npm registry](https://registry.npmjs.org) <br>
- [PyPI](https://pypi.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash snippets, JSON SBOM examples, and vulnerability-check output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local SBOM JSON files and may query public OSV, npm, and PyPI services for package metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
