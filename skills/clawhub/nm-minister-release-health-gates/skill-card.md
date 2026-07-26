## Description: <br>
Standardizes release approvals with GitHub-aware checklists and deployment gates for production release readiness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release managers, and operations teams use this skill before production deployment to evaluate release gates, document waiver approvals, and prepare PR or tracker-facing readiness summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to update PR comments, tracker tasks, and release artifacts in a repository. <br>
Mitigation: Use it only in repositories and trackers where those changes are intended, and review suggested updates before applying them. <br>
Risk: Release gate summaries can be incomplete or misleading if source issue, check, deployment, or tracker data is stale. <br>
Mitigation: Verify GitHub checks, deployment status, blocker lists, waiver approvals, and rollout scorecards before using the output for a production release decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-minister-release-health-gates) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown checklists and release-readiness summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces release gate snippets, QA handshake summaries, and rollout scorecards for review before use in PRs, issues, or trackers.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
