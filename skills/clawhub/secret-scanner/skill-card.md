## Description: <br>
Detect API keys, tokens, and credentials in code with 50+ patterns, entropy analysis, and multiple report formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security teams, maintainers, developers, and CI pipeline owners use this skill to scan files or directories for leaked secrets, review findings, and emit reports that can be used in development workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled CI verifier can execute Python files from target folders. <br>
Mitigation: Use the documented secret_scanner.py workflow for normal scanning, and run ci/verify_product.py only in a disposable sandbox with no network access and no sensitive environment variables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/secret-scanner) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>
- [Project repository](https://github.com/itsPremkumar/secret-scanner) <br>
- [Source script](https://raw.githubusercontent.com/itsPremkumar/secret-scanner/main/secret_scanner.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, guidance] <br>
**Output Format:** [CLI text, JSON findings, and SARIF report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are redacted for CI logs; scan output can be filtered by severity.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
