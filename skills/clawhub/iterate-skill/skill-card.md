## Description:

Iterate guides an AI coding assistant through multi-round, multi-dimension code review and repair, or defensive incremental coding with checks and a convergence gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill with AI coding assistants to review and improve a project across multiple quality dimensions, or to complete incremental coding tasks using defensive checks. It helps the assistant fix small issues, request approval for architectural changes, validate work, and report the outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance tools may change files outside the selected project, and installation safeguards may not behave as documented.

Mitigation: Prefer waiting for the directory-containment and installer-prompt fixes. If proceeding, use a disposable checkout without linked assistant directories, select the installation target explicitly, and review executable configuration.

Risk: Automatic repository changes and update paths may weaken review or release verification.

Mitigation: Keep automatic merge and push disabled, and avoid the source-checkout updater when relying on verified releases.

Risk: Maintainer signing and publishing helpers handle credentials.

Mitigation: Review those helpers separately before using them and protect any credentials they access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Project repository](https://github.com/jingzhao-l/iterate-skill)
- [npm installer](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Code and project-file changes, configuration, and Markdown summaries or review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update project files and run configured validation commands; merge and push are opt-in and disabled by default.]

## Skill Version(s):

3.11.0 (source: SKILL.md frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
