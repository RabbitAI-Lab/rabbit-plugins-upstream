## Description: <br>
cicd-aiops helps agents inspect and operate self-managed GitLab and self-hosted Gitea CI/CD servers, including projects, pipelines, runners, artifacts, RCA workflows, and governed writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and CI/CD operators use this skill to investigate self-managed GitLab or self-hosted Gitea pipeline failures, runner health, storage bloat, stale work, and selected governed operations such as retrying or canceling pipelines, pausing runners, deleting artifacts, and updating branch protection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact write tools can modify CI/CD state, including artifact deletion, runner changes, pipeline cancellation, and branch-protection updates. <br>
Mitigation: Install with least-privilege tokens, prefer read-only tokens for observation, and require external approval practices before enabling write scopes. <br>
Risk: The skill does not enforce its own read-only mode or approval gate for writes. <br>
Mitigation: Control authorization through GitLab or Gitea token scopes and agent policy, and review audit records for executed operations. <br>
Risk: Long-lived plaintext MCP configuration for CICD_AIOPS_MASTER_PASSWORD can expose the encrypted secret store password. <br>
Mitigation: Use safer secret-injection methods where available and avoid storing the master password in persistent plaintext client configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/cicd-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/CICD-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown, text, JSON-like tool results, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call CI/CD server APIs through configured tools; listings can be truncated and some operations are platform-specific.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
