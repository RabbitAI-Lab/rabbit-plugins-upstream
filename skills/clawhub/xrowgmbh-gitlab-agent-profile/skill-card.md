## Description: <br>
Maintain the GitLab agent profile page and static contribution performance chart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to keep GitLab profile assets current with monthly contribution statistics, charts, and proof records for selected GitLab projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses GitLab credentials to read project activity and update profile assets. <br>
Mitigation: Use a least-privilege GitLab token scoped only to the intended projects and rotation policy. <br>
Risk: Generated assets and proof records can overwrite local files or lead to unintended repository changes. <br>
Mitigation: Keep output paths inside the intended assets directory, review diffs, and prefer a branch or merge-request flow before publishing changes. <br>
Risk: The optional cron can run repeatedly and automate updates before review. <br>
Mitigation: Enable scheduled runs only after manual review and monitor the generated changes from initial runs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile) <br>
- [xrowgmbh Publisher Profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance plus generated SVG, WebP, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab, python3, and a GitLab token; default outputs are written under assets/.] <br>

## Skill Version(s): <br>
1.77.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
