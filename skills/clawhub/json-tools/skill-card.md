## Description: <br>
Validate, format, query, diff, filter, flatten, merge JSON files with dot-notation paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and agents use Json Tools to validate, format, query, diff, filter, flatten, and merge local JSON files with dot-notation paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes a CI verifier that can execute Python files from target folders. <br>
Mitigation: Run ci/verify_product.py only in a sandbox and avoid using it on untrusted folders or in environments with secrets. <br>
Risk: This is a third-party JSON CLI package with a suspicious security verdict in the server scan. <br>
Mitigation: Install only if you trust the publisher and intend to use the advertised local JSON operations. <br>


## Reference(s): <br>
- [Json Tools on ClawHub](https://clawhub.ai/itspremkumar/skills/json-tools) <br>
- [JSON Toolkit README](artifact/README.md) <br>
- [json_tools.py source download](https://raw.githubusercontent.com/itsPremkumar/json-tools/main/json_tools.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [CLI text and JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read JSON from files or stdin and can write merged JSON to a file when requested.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
