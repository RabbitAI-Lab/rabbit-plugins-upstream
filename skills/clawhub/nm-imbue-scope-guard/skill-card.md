## Description: <br>
Scores feature worthiness and enforces branch-size limits against overengineering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use scope-guard during brainstorming, planning, and execution to score proposed features, compare them with backlog items, and keep branches within size budgets before implementing or deferring work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default GitHub issue and Discussion publication can expose planning context or change repositories without enough user control. <br>
Mitigation: Make GitHub publication opt-in, confirm repository visibility, redact sensitive planning details, and review or disable the issue and Discussion steps before use. <br>
Risk: Broad automatic triggers could apply scope enforcement or publication workflows in situations where the user did not intend them. <br>
Mitigation: Avoid broad automatic triggers and require explicit user confirmation before repository-changing actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-scope-guard) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>
- [Decision framework](modules/decision-framework.md) <br>
- [GitHub integration](modules/github-integration.md) <br>
- [Anti-overengineering rules](modules/anti-overengineering.md) <br>
- [Branch threshold management](modules/branch-management.md) <br>
- [Baseline testing scenarios](modules/baseline-scenarios.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with scoring tables, checklists, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate GitHub issue and Discussion content for deferred work when enabled.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
