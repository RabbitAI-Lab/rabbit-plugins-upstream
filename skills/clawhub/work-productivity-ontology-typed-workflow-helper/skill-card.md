## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical ontology-style workflows, checklists, analysis, code changes, and decision support for work-productivity needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, skill authors, maintainers, and AI-agent users use this skill to turn ontology-style work-productivity requests into concrete local-friendly workflows, artifacts, checklists, analysis, code changes, or decision support. It is aimed at clarifying requirements, reducing manual coordination, and validating the result against explicit success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to be selected automatically for loosely related workflow or knowledge-graph requests.

Mitigation: Narrow the trigger keywords or disable implicit invocation before broad deployment when precise routing is required.

Risk: The skill can produce workflows, code changes, shell commands, or configuration guidance that may be incorrect for a user's environment.

Mitigation: Review generated outputs before applying them and verify them against the stated success criteria and local constraints.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper)
- [Publisher Profile](https://clawhub.ai/user/kyro-ma)
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)
- [Popular ClawHub skill demand: Multi Search Engine](https://clawhub.ai/skills/multi-search-engine)
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix)
- [Popular ClawHub skill demand: Skill Creator](https://clawhub.ai/skills/skill-creator)
- [Popular ClawHub skill demand: Notion](https://clawhub.ai/skills/notion)
- [HarmonyOS developer community](https://segmentfault.com/brand/harmonyos-next)
- [SegmentFault JavaScript tag](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript tag](https://segmentfault.com/t/typescript)
- [ONES R&D management](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- [Comp 3710 Artificial Intelligence](https://segmentfault.com/a/1190000041581431)
- [Comparison of four LLM text knowledge graph construction methods](https://segmentfault.com/a/1190000044569069)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code, shell command, configuration, checklist, and analysis blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and follow-up work when useful.]

## Skill Version(s):

0.20260908.51704 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
