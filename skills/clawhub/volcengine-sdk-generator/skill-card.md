## Description: <br>
Generates Volcengine SDK examples by locating an API through API Explorer search, fetching its swagger, and calling the make-code API with user-provided Params. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate Volcengine SDK call examples in Python, Go, Java, PHP, cURL, or Node.js and to answer SDK configuration questions such as credentials, retries, proxy settings, signing, and response handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reference guidance includes unsafe HTTP and SSL-disable examples without clear warnings. <br>
Mitigation: Use HTTPS and certificate verification for normal use; only disable SSL verification or switch to HTTP in tightly controlled local testing. <br>
Risk: User-supplied Params may contain real secrets sent to the make-code endpoint. <br>
Mitigation: Keep credentials in environment variables or approved credential providers, and avoid placing live secrets in API parameters. <br>


## Reference(s): <br>
- [Go SDK Integration Reference](references/sdk-integration-go.md) <br>
- [Java SDK Integration Reference](references/sdk-integration-java.md) <br>
- [Node.js SDK Integration Reference](references/sdk-integration-nodejs.md) <br>
- [PHP SDK Integration Reference](references/sdk-integration-php.md) <br>
- [Python SDK Integration Reference](references/sdk-integration-python.md) <br>
- [Volcengine API Explorer Common API](https://api.volcengine.com/api/common) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with code blocks and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated examples may include mocked required parameters when user-provided Params are incomplete.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
