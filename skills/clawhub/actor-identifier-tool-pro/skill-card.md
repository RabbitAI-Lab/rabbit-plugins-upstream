## Description: <br>
Provides an agent workflow for Git repository collaboration analysis, including multi-repository aggregation, custom metrics, CI/CD reporting, historical trend comparison, and team process discussion prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and team leads use this skill to generate repository-level collaboration reports, CI analysis workflows, custom metric configurations, and process-improvement prompts without using the results for individual performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write local reports, commit and push repository changes, send Slack notifications, and use repository or Slack tokens. <br>
Mitigation: Use it only on approved repositories, review generated reports and CI changes before publishing, and run with least-privilege repository and Slack credentials. <br>
Risk: Custom metric queries can introduce command-execution risk. <br>
Mitigation: Require explicit review and allow-list validation for every custom metric query before execution. <br>
Risk: The security evidence says the documentation understates write, network, credential, and command-execution behavior. <br>
Mitigation: Review the release security guidance before installing or using the skill in CI. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/actor-identifier-tool-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local repository-analysis reports, CI workflow snippets, custom metric configuration, and team discussion prompts.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
