## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update GitLab profile assets with monthly merge request, direct commit, and contribution score data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab credentials and may push generated repository changes.

Mitigation: Review diffs before pushing and keep scheduled autonomous runs disabled unless autonomous updates are intended.

Risk: The WebP conversion path may run unpinned npm code as a fallback.

Mitigation: Prefer pinned or preinstalled image conversion tools, or remove the npm fallback before routine use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [ClawHub Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands; generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI authentication with GITLAB_TOKEN and writes profile assets under configurable output paths.]

## Skill Version(s):

1.86.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
