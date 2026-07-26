## Description: <br>
Query HashiCorp Nomad clusters. List jobs, nodes, allocations, evaluations, and services. Read-only operations for monitoring and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danfedick](https://clawhub.ai/user/danfedick) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to query HashiCorp Nomad cluster state, inspect jobs, allocations, nodes, evaluations, services, namespaces, and variables, and troubleshoot incidents with read-only CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Nomad allocation logs, variables, and cluster metadata can contain confidential or sensitive information. <br>
Mitigation: Use a least-privilege read-only Nomad ACL token where possible, treat query output as confidential, and redact sensitive values before sharing results. <br>
Risk: Commands may query the wrong Nomad address, namespace, or region if the environment is misconfigured. <br>
Mitigation: Verify NOMAD_ADDR, NOMAD_NAMESPACE, and NOMAD_REGION before running commands against a cluster. <br>


## Reference(s): <br>
- [ClawHub Nomad skill page](https://clawhub.ai/danfedick/skills/nomad) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Nomad CLI query patterns, optional JSON output variants, filtering examples, and environment variable guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
