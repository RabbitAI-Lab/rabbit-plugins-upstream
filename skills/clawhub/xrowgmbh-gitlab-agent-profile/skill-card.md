## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to refresh a GitLab agent profile with monthly contribution statistics, static chart assets, and a JSON proof file for public and anonymized private activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be configured for persistent scheduled agent execution.

Mitigation: Remove the scheduled cron entry or keep it manually controlled, disabled, and reviewed before enabling unattended runs.

Risk: The WebP generation path can dynamically execute an unpinned npm package fallback.

Mitigation: Prefer reviewed ImageMagick or pinned Python dependencies, or pin and review `sharp-cli` and its dependencies before allowing the npm fallback.

Risk: GitLab project discovery can cover more repositories than intended when a broad root group is used.

Mitigation: Use an explicit `GITLAB_AGENT_PROFILE_PROJECTS` list or a tightly scoped root group with the least-privileged GitLab token possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands; generated assets include SVG, WebP, and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI authentication and writes profile assets under the configured workspace.]

## Skill Version(s):

1.91.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
