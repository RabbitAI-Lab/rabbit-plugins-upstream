## Description: <br>
Create, debug, and manage CI/CD pipelines with GitHub Actions for automated testing, deployment, releases, workflow patterns, secrets management, caching, matrix builds, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create, debug, and maintain GitHub Actions workflows for CI, deployment, releases, Docker publishing, npm publishing, caching, matrix builds, and workflow troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated workflow files can affect deployments, releases, package publishing, Docker publishing, or secret handling. <br>
Mitigation: Review any generated .github/workflows files before committing them, and use least-privilege tokens, environment protections, trusted or pinned actions, staging tests, and manual approvals for production systems or public artifacts. <br>
Risk: Secrets examples can be misapplied in workflows that access production credentials. <br>
Mitigation: Keep secrets scoped to the minimum required environment or job, avoid exposing secret values in logs, and require reviewer approval for protected environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gitgoodordietrying/skills/cicd-pipeline) <br>
- [npm Registry](https://registry.npmjs.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML workflow examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples target GitHub Actions and may require gh or git for CLI workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
