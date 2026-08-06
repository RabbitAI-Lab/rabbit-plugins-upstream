## Description: <br>
Review plugin quality with tiered checks and dependency scoping for PR and pre-release audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release maintainers use this skill to scope and run tiered quality reviews for plugin changes before branch work, pull requests, and releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words may cause the skill to activate during ordinary review requests. <br>
Mitigation: Invoke or configure the skill specifically for plugin-review tasks when broad review activation is not desired. <br>
Risk: Suggested make targets and local Python scripts execute code from the checked-out repository. <br>
Mitigation: Run command examples only in repositories and branches that the user trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-plugin-review) <br>
- [Plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables, verdicts, scorecards, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CI/CD exit-code guidance for quality gate mode.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
