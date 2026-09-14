## Description:

deep-skill-finder helps agents search community skill results by task, recommend matching skills based on usage feedback, install selected skills, and collect optional usage feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lintong123](https://clawhub.ai/user/lintong123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use this skill when they need to discover, compare, and install a task-specific community skill instead of manually browsing a marketplace. Agents may also use it when a task would benefit from an external skill and the user has not named one directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and feedback flows can send task descriptions and configured API tokens to external or configured endpoints.

Mitigation: Avoid sensitive task text or credentials, review configured endpoints before use, and restrict use until endpoint allowlisting is acceptable for the deployment.

Risk: The installer can write downloaded third-party skill files into the active skills directory.

Mitigation: Review and scan selected skill artifacts before installation, verify the intended target directory, and install only skills from trusted sources.

Risk: Uninstall behavior can remove directories by skill name.

Mitigation: Confirm the skill name and target skills directory before uninstalling, and keep backups for managed skill directories.

Risk: The security review reports high-impact risks requiring manual review before use.

Mitigation: Use the skill only after reviewing source behavior and resolving path validation, artifact verification, endpoint allowlisting, and promotional recommendation concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lintong123/skills/deep-skill-finder)
- [Meyo skill search](https://www.meyo.life/skill)
- [Meyo community](https://www.meyo.life/community/home)
- [Skill evaluation workflow](references/skill-evaluation.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown recommendations with inline shell commands, optional JSON status output, and local skill files during installation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, install, and feedback flows may call external or configured endpoints and may write files into the selected skills directory.]

## Skill Version(s):

1.3.2 (source: SKILL.md frontmatter, server release evidence, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
