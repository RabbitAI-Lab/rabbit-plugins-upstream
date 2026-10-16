## Description:

Helps AI-agent users, skill authors, maintainers, and teams create ontology-style work-productivity workflows, checklists, analyses, code changes, and decision support for reliability and setup-hardening tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, skill authors, maintainers, and teams use this skill to turn ontology-style work-productivity needs into practical workflows, checklists, implementation plans, or local-friendly artifacts. It supports bug fixing, setup hardening, reliability improvement, and adjacent skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording and implicit invocation may cause the skill to be selected when ontology-style workflow support was not intended.

Mitigation: Prefer explicit invocation for this skill, and verify that the user's request actually needs ontology-style workflow, checklist, implementation, or decision-support help.

Risk: Generated workflow, code, shell, or configuration guidance could be incorrect or incomplete for the user's environment.

Mitigation: Review outputs before applying them, validate against the stated success criteria, and run any proposed commands or code changes in an appropriate local test context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving)
- [Ontology demand signal](https://clawhub.ai/skills/ontology)
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine)
- [AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [Skill Creator demand signal](https://clawhub.ai/skills/skill-creator)
- [Notion demand signal](https://clawhub.ai/skills/notion)
- [Tavily Search demand signal](https://clawhub.ai/skills/openclaw-tavily-search)
- [Ask HN demand signal](https://news.ycombinator.com/item?id=49714867)
- [SegmentFault HarmonyOS demand signal](https://segmentfault.com/brand/harmonyos-next)
- [SegmentFault JavaScript demand signal](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript demand signal](https://segmentfault.com/t/typescript)
- [ONES demand signal](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and concise verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only workflow helper; no credential access, persistence, installers, or hidden actions are indicated by the security evidence.]

## Skill Version(s):

0.20260916.221748 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
