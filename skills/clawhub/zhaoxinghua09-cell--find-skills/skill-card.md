## Description:

场景驱动+关键词双模式技能发现工具，当用户用自然语言描述场景或明确要求查找、安装技能时，联合搜索官方内置、本地已安装、SkillHub、虾评、GitHub 和 ClawHub 来源并推荐合适技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and WorkBuddy or CodeBuddy users use this skill to discover relevant agent skills from natural-language task descriptions, compare local and remote options, and receive installation guidance when a remote skill is selected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install remote skills into persistent local skill directories.

Mitigation: Review the publisher, source, version, and checksum before installing any remote skill, and avoid ZIP or npx installation paths unless independently verified.

Risk: The skill may read local skill metadata, contact multiple remote marketplaces, and use a GitHub token when one is present.

Mitigation: Run it only in trusted workspaces, limit any GitHub token scope, and review outbound marketplace or repository calls before execution.

Risk: The skill steers agent routing and includes mandatory promotional content in outputs.

Mitigation: Inspect recommendations and generated output before relying on them, and remove or disable the skill if the routing or promotional behavior is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/find-skills)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [SkillHub search API endpoint](https://lightmake.site/api/v1/search)
- [Xiaping skill marketplace API base](https://xiaping.coze.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown recommendations with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ranked skill recommendations, match rationale, source labels, installation commands, and client-specific installation paths.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
