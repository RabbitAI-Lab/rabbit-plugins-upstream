## Description: <br>
github-manager helps agents manage GitHub repositories with batch issue and pull request operations, GraphQL queries, automation workflows, team dashboards, webhook management, and security audit guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to plan and execute GitHub repository maintenance, team workflow automation, webhook setup, reporting, and security audit tasks across one or more repositories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide broad repository or organization-changing actions through GitHub tokens and automation. <br>
Mitigation: Use the narrowest GitHub token scopes possible, review permissions before installation, and verify automation rules before enabling them. <br>
Risk: Batch issue, pull request, migration, or webhook operations can affect many repositories or records at once. <br>
Mitigation: Run dry-runs before batch operations, review planned changes, and use confirmation or rollback procedures where available. <br>
Risk: Webhook endpoints, dashboards, and generated reports may expose repository or team information beyond the intended audience. <br>
Mitigation: Send webhooks only to trusted HTTPS endpoints and restrict dashboard or report outputs to the intended machine or team. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/github-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell, JSON, YAML, and GraphQL examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitHub CLI and gh-manager commands, automation rules, dashboard or report instructions, and audit guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
