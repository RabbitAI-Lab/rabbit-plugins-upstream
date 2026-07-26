## Description: <br>
Use when maintaining or using the UnifyPort Node.js SDK; covers the Device API client, public contract, generated code, errors, retries, and the new API workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unifyport](https://clawhub.ai/user/unifyport) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate @unifyport/sdk-node into Node.js or TypeScript applications, or to maintain the SDK contract, generated code, tests, authentication, retries, pagination, and error handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API credentials or request details could be exposed if copied into source, logs, generated files, tool inputs, or committed configuration. <br>
Mitigation: Provide credentials only through approved runtime environment variables and avoid printing, persisting, or logging complete requests, responses, or client configuration. <br>
Risk: A live Device API call could have unintended effects if run only to validate installation. <br>
Mitigation: Prefer type checking and mocked transport tests; execute live calls only when the user explicitly requests them and supplies an approved test environment. <br>
Risk: Manual or inferred API contract changes could misrepresent authentication, side effects, retries, secrets, destructive behavior, or public types. <br>
Mitigation: Base contract changes on approved public API schemas and release notes, regenerate code, review the diff, and run the repository's public contract checks. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/unifyport/skills/unifyport-node-sdk) <br>
- [@unifyport/sdk-node npm Package](https://www.npmjs.com/package/@unifyport/sdk-node) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm for applicable workflows; live API requests require user- or deployment-supplied UnifyPort environment credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
