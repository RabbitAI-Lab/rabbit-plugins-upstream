## Description: <br>
Provides a static knowledge graph that agents can use as a speculative reasoning lens for paradox analysis, open scientific and philosophical questions, high-complexity forecasting, AI safety discussions, and strategic reasoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matthiasbeckmann987-spec](https://clawhub.ai/user/matthiasbeckmann987-spec) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to load graph.json and produce graph-grounded Markdown reasoning for paradoxes, speculative scientific or philosophical questions, complex forecasts, strategic problems, and AI safety architecture discussions. Outputs should be treated as model-guided analysis rather than factual authority or policy advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The graph can produce prescriptive guidance for indirect persuasion or behavior-change framing without strong consent safeguards. <br>
Mitigation: Use it only with explicit user consent and independent review; do not use it for covert persuasion, recommendation steering, behavior-change programs, financial decisions, or AI self-improvement workflows. <br>
Risk: Graph-grounded outputs may present speculative philosophical or scientific reasoning as if it were factual or settled. <br>
Mitigation: Frame outputs as one perspective, preserve confidence and limits, and require external evidence before using conclusions as facts, safety policy, or operational decisions. <br>
Risk: The artifact includes sensitive historical and psychological-manipulation topics that can lose safety context when summarized locally or mechanically. <br>
Mitigation: Keep critical context and condemnation of harmful narratives with any excerpted node, and review summaries before reuse in downstream agent prompts or user-facing material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/matthiasbeckmann987-spec/skills/beckmann-knowledge-graph) <br>
- [Publisher profile](https://clawhub.ai/user/matthiasbeckmann987-spec) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Readme.md](artifact/Readme.md) <br>
- [graph.json](artifact/graph.json) <br>
- [Explanation for the ClawHub scanner.md](artifact/Explanation for the ClawHub scanner.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown graph-grounded answer with relevant nodes, reasoning path, confidence limits, and follow-up questions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a static JSON graph with 681 entities and 1146 relations; outputs should include confidence and limits and avoid presenting graph-derived speculation as fact.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release, SKILL.md frontmatter, and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
