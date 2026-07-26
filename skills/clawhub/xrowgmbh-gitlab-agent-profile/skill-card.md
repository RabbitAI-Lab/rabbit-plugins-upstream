## Description: <br>
Maintain the GitLab agent profile page and static contribution performance chart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to keep a GitLab profile repository updated with monthly contribution charts and proof records for owner and agent activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses GitLab credentials that may read configured projects. <br>
Mitigation: Use a least-privilege GitLab token and limit configured projects to repositories needed for the profile update. <br>
Risk: The skill can run unattended and commit or push generated profile assets. <br>
Mitigation: Run it in a dedicated profile repository and review the cron configuration before enabling scheduled execution. <br>
Risk: Output paths and image conversion tooling can affect local files or invoke optional external converters. <br>
Mitigation: Keep output paths relative to the intended workspace and avoid the npm or ImageMagick conversion fallback unless the tooling is pinned or sandboxed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Files] <br>
**Output Format:** [Markdown guidance plus generated SVG, WebP, and JSON asset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GitLab CLI authentication and configurable environment variables for project selection, output paths, owner, agent, and month count.] <br>

## Skill Version(s): <br>
1.75.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
