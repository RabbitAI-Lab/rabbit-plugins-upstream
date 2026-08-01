## Description: <br>
Maintain the GitLab agent profile page and static contribution performance chart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to update a GitLab profile repository with monthly contribution performance charts and proof records for owner and agent activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses GitLab credentials while collecting contribution data and updating repository assets. <br>
Mitigation: Install it only in a dedicated profile repository with a least-privilege GitLab token. <br>
Risk: Scheduled execution can repeatedly write generated files and support repository pushes with limited safeguards. <br>
Mitigation: Keep the cron disabled until schedule, output path containment, manual review, and branch protection are configured. <br>
Risk: Chart conversion depends on local converter tooling that may vary by environment. <br>
Mitigation: Approve the converter dependencies before enabling automated runs. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile) <br>
- [Publisher profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, Configuration instructions] <br>
**Output Format:** [Markdown guidance with generated SVG, WebP, and JSON assets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab and python3, uses GITLAB_TOKEN, and writes profile assets plus JSON proof records.] <br>

## Skill Version(s): <br>
1.78.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
