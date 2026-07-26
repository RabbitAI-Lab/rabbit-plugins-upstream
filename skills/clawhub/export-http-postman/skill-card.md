## Description: <br>
Exports an HTTP API endpoint from the current work project into a Postman-importable collection JSON file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[extraskittles](https://clawhub.ai/user/extraskittles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect project route definitions and export selected HTTP endpoints as Postman v2.1 collection JSON. It helps preserve inferred methods, paths, query parameters, headers, body examples, and service-domain choices while using placeholders for sensitive or environment-specific values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects project code to infer routes, request fields, and service domains. <br>
Mitigation: Review the selected endpoint, inferred base URL, and generated collection before using or sharing the output. <br>
Risk: A generated collection could include real tokens, cookies, identifiers, or other secrets if they are copied from local project files. <br>
Mitigation: Use placeholders for sensitive values and reject exports that include real credentials or private identifiers. <br>
Risk: Stored service-domain mappings can influence future Postman base URLs. <br>
Mitigation: Review references/domains.md when base URLs matter and confirm domains before adding new service mappings. <br>


## Reference(s): <br>
- [Stored Service Domains](references/domains.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Postman Collection v2.1 JSON file with a concise Markdown status summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update stored service-domain mappings after user confirmation; generated values should use placeholders for secrets and environment-specific identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
