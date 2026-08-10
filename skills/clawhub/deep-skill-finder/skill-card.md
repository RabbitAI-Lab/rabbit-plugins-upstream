## Description:

Finds relevant community skills for a user's task, presents ranked recommendations, and installs the selected skill into the agent's local skills directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lintong123](https://clawhub.ai/user/lintong123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover community skills that match a task, review a small ranked recommendation list, and install a selected skill into the active agent environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote search can send the user's task description and a persistent client identifier to Meyo.

Mitigation: Avoid submitting sensitive task details and review the configured Meyo endpoint before use.

Risk: If Meyo credentials or MEYO_API_URL are configured, requests may authenticate to the selected endpoint.

Mitigation: Use Meyo credentials only with trusted endpoints and verify local Meyo configuration before running the scripts.

Risk: The installer writes selected community skill files into the agent environment without strong package containment checks.

Mitigation: Install only recommendations from trusted publishers and review downloaded skill files before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lintong123/skills/deep-skill-finder)
- [Meyo skill search](https://www.meyo.life/skill)
- [Meyo community](https://www.meyo.life/community/home)
- [Meyo community skills](https://www.meyo.life/community/square/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown recommendation table with command-line search and installation steps; installer status may include JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search may send the task description and a persistent client identifier to Meyo; installation writes selected community skill files into the target skills directory.]

## Skill Version(s):

1.2.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
