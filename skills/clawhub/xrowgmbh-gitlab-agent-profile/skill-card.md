## Description: <br>
Maintain the GitLab agent profile page and static contribution performance chart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to keep GitLab profile assets current with monthly contribution statistics. It prepares static chart and proof-record assets from GitLab merge request and commit activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a GitLab token and publish repository changes. <br>
Mitigation: Use a minimally scoped GitLab token, run the update manually first, and review generated assets before pushing. <br>
Risk: Configured output paths may write outside the intended workspace. <br>
Mitigation: Keep chart, WebP, and proof-record output paths under the profile repository. <br>
Risk: WebP conversion may invoke an external converter or package dependency. <br>
Mitigation: Use a trusted converter such as ImageMagick or pin the WebP conversion dependency. <br>
Risk: The bundled cron can run unattended if enabled. <br>
Mitigation: Enable the cron only when unattended publishing is intended. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile) <br>
- [xrowgmbh Publisher Profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, files, JSON, guidance] <br>
**Output Format:** [Markdown instructions plus generated SVG, WebP, and JSON proof files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GitLab CLI authentication and configurable environment variables for workspace, project, owner, agent, month window, and output paths.] <br>

## Skill Version(s): <br>
1.78.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
