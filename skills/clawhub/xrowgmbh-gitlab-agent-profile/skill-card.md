## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab agent profile current with monthly contribution statistics, static chart assets, and a JSON proof file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a GitLab token through the GitLab CLI to read contribution data.

Mitigation: Use scoped GitLab credentials and confirm the authenticated account before running the update helper.

Risk: The update routine writes profile assets and may lead to remote pushes when the generated assets are committed.

Mitigation: Review generated diffs before committing or pushing, and constrain output paths with the documented environment variables.

Risk: The bootstrap cron creates recurring automation if enabled.

Mitigation: Keep the cron disabled unless recurring updates are intended, and review its schedule and workspace target before enabling it.

Risk: The WebP conversion path can fall back to npm-based tooling.

Mitigation: Prefer controlled ImageMagick or Python image dependencies, or ensure npm dependencies are pinned and trusted before allowing that fallback.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [files, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes profile assets under assets/ by default and uses GitLab-related environment variables for project, owner, agent, month, and output settings.]

## Skill Version(s):

1.84.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
