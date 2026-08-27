## Description:

Skill-Kit helps Claude Code users create, lint, merge, upgrade, route, publish, and automate multi-topic skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Skill-Kit to author, validate, convert, organize, and maintain Claude Code skills, including frontmatter linting, topic routing, dependency graphing, publication checks, and hook trigger generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger workflow can persistently change Claude hook scripts and settings.

Mitigation: Use dry-run first, review generated hook scripts and the settings.json diff, and compile triggers only from trusted skills.

Risk: Skill installation, backup, cleanup, and conversion workflows can alter local Claude skill or agent files.

Mitigation: Review the publisher and skill contents before global installs, avoid no-confirm third-party installs, and inspect backup or delete operations before allowing cleanup.

Risk: Generated or suggested skill-management changes may introduce incorrect frontmatter, routing, or publication guidance.

Mitigation: Run the skill's lint and review procedures, then scan and manually review changed skills before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/skill-kit)
- [Skills.sh](https://skills.sh/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and generated configuration or hook files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or generate changes to Claude skill files, hook scripts, and settings when invoked for those workflows.]

## Skill Version(s):

0.7.1 (source: server release metadata and changelog, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
