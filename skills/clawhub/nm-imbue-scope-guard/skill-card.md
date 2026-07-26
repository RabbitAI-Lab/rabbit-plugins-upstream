## Description: <br>
Scores feature worthiness and enforces branch-size limits against overengineering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to evaluate proposed features before and during implementation. It helps agents score business value against complexity, compare work against backlog priorities, and keep branches within documented scope limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer an agent to create GitHub issues and publish detailed Discussion context for deferred work, which may expose private project reasoning. <br>
Mitigation: Require explicit approval before GitHub issue or Discussion creation, preview the exact content, and default to local backlog notes for sensitive repositories. <br>
Risk: The security scan marked the release suspicious because the workflow encourages external writes even though the skill is mostly planning and scope-control guidance. <br>
Mitigation: Install only when scope discipline is desired, and review generated commands and publication steps before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-scope-guard) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Decision framework](modules/decision-framework.md) <br>
- [Anti-overengineering rules](modules/anti-overengineering.md) <br>
- [Branch threshold management](modules/branch-management.md) <br>
- [GitHub issue integration](modules/github-integration.md) <br>
- [Baseline testing scenarios](modules/baseline-scenarios.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with scoring tables, checklists, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose backlog entries, GitHub issue content, and GitHub Discussion content for deferred work.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
