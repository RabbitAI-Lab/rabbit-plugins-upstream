## Description: <br>
Azure Identity SDK for Python authentication guidance for DefaultAzureCredential, managed identity, service principals, and token caching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill when adding Microsoft Entra ID authentication to Python applications with Azure SDK clients. It helps select and configure Azure Identity credential types for local development, CI, and Azure-hosted workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential examples could lead users to expose Azure tenant IDs, client IDs, or client secrets in prompts, logs, or committed files. <br>
Mitigation: Use placeholders in generated examples, keep Azure secrets out of prompts and logs, and store production credentials in approved secret-management systems. <br>
Risk: Incorrect credential choice or over-privileged service principals can expand access beyond the intended Azure workload. <br>
Mitigation: Prefer managed identity for Azure-hosted workloads, use least-privilege service principals when secrets are required, and review credential configuration before deployment. <br>
Risk: Unpinned Azure Identity package versions can make production authentication behavior change unexpectedly. <br>
Mitigation: Pin azure-identity versions in production projects and test authentication flows after dependency updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-identity-py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes credential selection guidance and environment variable examples; users should avoid exposing real secrets in prompts, logs, or generated files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
