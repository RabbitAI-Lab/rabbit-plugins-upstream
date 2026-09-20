## Description:

Design better AI skills with proven architecture patterns, including Workflow vs Agent selection, workflow pattern choice, SKILL.md structure, and governance-aware quality review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to choose a skill architecture, select workflow patterns, write maintainable SKILL.md files, and review skills against a governance-aware checklist before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loose host auto-triggering may load design-checklist context for tasks that are only loosely related to skill building.

Mitigation: Invoke the skill explicitly for skill-design or skill-review work, and tune host routing triggers when false positives are observed.

Risk: Architecture recommendations can be applied too broadly if treated as a substitute for project-specific review.

Mitigation: Review recommendations against the included quality checklist and the target skill's actual behavior before publishing or deployment.

## Reference(s):

- [Skill Design Guide on ClawHub](https://clawhub.ai/haiyangchenbj/skill-design-guide-skill)
- [Agent Design Research](references/agent-design-research.md)
- [Anthropic Tool Design](references/anthropic-tool-design.md)
- [Pattern Details](references/pattern-details.md)
- [Platform Compatibility](references/platform-compatibility.md)
- [Quality Checklist](references/quality-checklist.md)
- [Anthropic - Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic - Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [LangChain Blog](https://blog.langchain.dev/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance, architecture recommendations, review reports, and checklist-driven notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no bundled executable code.]

## Skill Version(s):

1.7.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
