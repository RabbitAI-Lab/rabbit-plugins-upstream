## Description:

Helps agent users, skill authors, maintainers, and teams turn ontology-style workflow needs into practical plans, checklists, analysis, implementation support, and verification notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to structure ontology-style workflow requests into actionable plans, templates, checklists, code changes, analysis, or decision support. It is intended for practical local-hardware-friendly workflow improvement, setup hardening, reliability work, and adjacent skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording and implicit invocation can make the skill appear in general workflow, knowledge-graph, or bug-fix conversations where it may not be the best fit.

Mitigation: Review whether the invocation is relevant before relying on its guidance, especially when the request is only loosely related to ontology-style or typed workflow planning.

Risk: Planning and implementation guidance can be incomplete or mismatched if the user's outcome, constraints, or success criteria are ambiguous.

Mitigation: State assumptions, ask only for materially missing inputs, and validate the final output against the user's success criteria.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving)
- [Ontology demand signal](https://clawhub.ai/skills/ontology)
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine)
- [AdMapix demand signal](https://clawhub.ai/skills/admapix)
- [Notion demand signal](https://clawhub.ai/skills/notion)
- [Hacker News demand signal](https://news.ycombinator.com/item?id=49308530)
- [OpenBKN relationship subgraph issue](https://github.com/openbkn-ai/bkn-foundry/issues/951)
- [OpenBKN cancel action execution issue](https://github.com/openbkn-ai/bkn-foundry/issues/949)
- [Sarvam Agents experience-to-skill issue](https://github.com/sarvamai/skills/issues/15)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, visible limits, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260816.40342 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
