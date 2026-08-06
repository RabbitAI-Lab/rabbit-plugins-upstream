## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn ontology-style workflow demand into practical workflows, artifacts, checklists, analyses, code changes, or decision support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI-agent users, skill authors, maintainers, and teams use this skill to structure ontology-style workflow requests into concrete plans, templates, checklists, analyses, code changes, or decision support. It is intended for practical local workflows that clarify assumptions, produce a usable artifact, and validate the result against stated success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill for general workflow, checklist, analysis, or implementation requests where ontology-specific help was not intended. <br>
Mitigation: Prefer explicit ontology or typed-workflow requests and review invocation routing before deployment. <br>
Risk: Generated workflows, code changes, shell commands, or configuration guidance may be wrong for a user's environment. <br>
Mitigation: Review outputs before use and validate them against the stated success criteria and local constraints. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub release page](https://clawhub.ai/kyro-ma/skills/work-productivity-ontology-typed-workflow-helper) <br>
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving) <br>
- [Ontology demand signal](https://clawhub.ai/skills/ontology) <br>
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine) <br>
- [AdMapix demand signal](https://clawhub.ai/skills/admapix) <br>
- [Wyro Hacker News demand signal](https://news.ycombinator.com/item?id=49134292) <br>
- [GitHub issue 493 demand signal](https://github.com/zig-utils/zig-js/issues/493) <br>
- [GitHub issue 492 demand signal](https://github.com/zig-utils/zig-js/issues/492) <br>
- [GitHub issue 489 demand signal](https://github.com/zig-utils/zig-js/issues/489) <br>
- [GitHub issue 487 demand signal](https://github.com/zig-utils/zig-js/issues/487) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, checklists, command snippets, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, limits, remaining risks, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.20260802.40421 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
