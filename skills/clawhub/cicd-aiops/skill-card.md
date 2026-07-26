## Description: <br>
Cicd Aiops helps agents operate self-managed GitLab and self-hosted Gitea CI/CD servers for pipeline, runner, artifact, release, branch-protection, and RCA workflows with governed read and write actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and SREs use this skill to inspect self-managed GitLab/Gitea CI/CD state, triage failed pipelines and runner queues, assess artifact bloat and stale work, and prepare governed actions such as retrying pipelines, pausing runners, updating branch protection, or deleting old artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact CI/CD writes using configured GitLab or Gitea access tokens. <br>
Mitigation: Start with read-only or tightly scoped tokens, require separate human approval before write actions, and widen token scopes only after validating the target setup. <br>
Risk: Artifact deletion is irreversible even when audit records capture destroyed counts and bytes. <br>
Mitigation: Use dry runs first, set an explicit age threshold, and review the deletion scope before confirming any artifact deletion. <br>
Risk: Governance depends on token scope, local audit logs, and agent/operator behavior rather than an enforced approval gate or read-only mode. <br>
Mitigation: Use server-side permissions as the primary control, review the audit log for write activity, and configure agent policy to avoid write tools during observe-only sessions. <br>
Risk: The artifact states the REST paths are mock-validated and not yet recorded as end-to-end tested against a live server. <br>
Mitigation: Run `cicd-aiops doctor` and verify representative read and write dry-run workflows against a non-production self-managed GitLab or Gitea instance before production use. <br>


## Reference(s): <br>
- [CICD-AIops homepage](https://github.com/AIops-tools/CICD-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/cicd-aiops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API-derived CI/CD summaries, RCA classifications, dry-run write plans, and configuration steps.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
