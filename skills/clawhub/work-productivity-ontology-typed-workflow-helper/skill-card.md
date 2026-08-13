## Description:

Helps AI-agent users, skill authors, maintainers, and teams create ontology-style productivity workflows, checklists, analysis, implementation support, and adjacent skill patterns for fixing bugs, improving safety, and improving reliability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and teams use this skill to turn ontology-style productivity needs into practical plans, workflows, checklists, analysis, code changes, or decision support. It is intended for work-productivity, knowledge graph, typed workflow, memory, composability, reliability, and bug-fix tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation may activate the skill for general productivity, knowledge graph, memory, or bug-fix requests where a narrower helper would be more appropriate.

Mitigation: Restrict implicit invocation when the platform supports it, or review activation behavior before enabling the skill in shared or production agent environments.

Risk: Workflow recommendations may introduce incorrect or misleading guidance if used without review.

Mitigation: Review generated plans, checklists, code, commands, and configuration before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving)
- [Ontology demand signal](https://clawhub.ai/skills/ontology)
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine)
- [AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [Notion demand signal](https://clawhub.ai/skills/notion)
- [Hacker News demand signal](https://news.ycombinator.com/item?id=49268880)
- [HarmonyOS developer community demand signal](https://segmentfault.com/brand/harmonyos-next)
- [JavaScript demand signal](https://segmentfault.com/t/javascript)
- [TypeScript demand signal](https://segmentfault.com/t/typescript)
- [ONES research management demand signal](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- [OntologyOps demand signal](https://segmentfault.com/a/1190000047947726)
- [Comp 3710 AI demand signal](https://segmentfault.com/a/1190000041581431)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Analysis]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, workflow outlines, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and next steps.]

## Skill Version(s):

0.20260813.40345 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
