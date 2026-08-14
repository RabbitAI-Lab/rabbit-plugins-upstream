## Description: <br>
Helps agents format and validate JSON data for improved readability and structure checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[HonestQiao](https://clawhub.ai/user/HonestQiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents can use this skill to prettify compact JSON, check whether input parses, and return structured formatting status while preparing configuration or data snippets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: JSON inputs may contain secrets or sensitive data that become visible to the agent during formatting. <br>
Mitigation: Avoid submitting credentials, tokens, or private data unless the agent environment is approved for that content. <br>
Risk: Documented path extraction or compression behavior may be incomplete or inconsistent. <br>
Mitigation: Verify outputs for path extraction or compression before relying on those features. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/HonestQiao/json-formatter) <br>


## Skill Output: <br>
**Output Type(s):** [text, code] <br>
**Output Format:** [JSON object with formatted JSON text, validity status, size, and paths when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Indentation defaults to 2 spaces when not specified; invalid input returns an error and valid=false.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
