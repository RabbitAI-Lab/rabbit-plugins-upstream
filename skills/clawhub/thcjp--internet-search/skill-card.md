## Description:

Provides agent guidance for using an internet_search tool to route categories, formulate queries, and perform multi-step information retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to structure internet search tasks, including query formulation, category routing, result checking, and follow-up retrieval steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and local file-access capabilities that are broader than its stated search-helper purpose.

Mitigation: Review the skill before installation and prefer a version that removes exec and narrows file access unless those capabilities are specifically required.

Risk: Search results and generated retrieval guidance can be incomplete, stale, or misleading.

Mitigation: Have the agent cite sources, compare multiple results, and ask a human reviewer to check important conclusions before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/internet-search)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub skill page](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search behavior depends on the host agent, network access, and available tools.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
