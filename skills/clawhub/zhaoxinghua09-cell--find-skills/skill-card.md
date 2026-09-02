## Description:

技能发现雷达 helps an agent interpret a user's skill-discovery request, search local and external skill sources, recommend matching skills, and support installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to find relevant agent skills from built-in, local, marketplace, GitHub, and ClawHub-style sources based on natural-language needs. It can return ranked recommendations with reasons and installation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send user search terms to external marketplaces and APIs.

Mitigation: Review search terms before remote lookup and avoid including sensitive project, customer, or credential information in skill-discovery prompts.

Risk: The skill can use a GitHub token from the environment for authenticated searches.

Mitigation: Use a narrowly scoped token when needed, and remove broad or unrelated GitHub credentials from the agent environment before running the skill.

Risk: The skill can install persistent skill content from third-party sources.

Mitigation: Inspect the recommended skill source, license, and security posture before installation, and prefer trusted or already-installed skills when available.

Risk: Local skill directory scans may expose information about installed capabilities and workspace configuration.

Mitigation: Run the skill only in workspaces where local skill inventory disclosure is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/find-skills)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with ranked recommendations, match rationale, source labels, and inline installation commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include external marketplace results, local skill paths, and installation steps.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
