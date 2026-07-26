## Description: <br>
知识图谱工具(免费版) helps a personal agent maintain a local JSON-backed knowledge graph, query entities and relationships, and produce compact KGML context summaries for later sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to structure personal notes, research material, and session memory as a local knowledge graph. It supports basic graph maintenance, queries, timeline/statistics views, and KGML summaries that an agent can carry into later conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags persistent agent-instruction changes and later context injection with unclear control boundaries. <br>
Mitigation: Review any changes to agent instruction files before use, keep generated summaries visible to the user, and install only when persistent KG context is expected. <br>
Risk: The skill can persist personal knowledge in local graph files and reuse it in later sessions. <br>
Mitigation: Avoid storing sensitive notes until local-only behavior is verified, add generated data files to gitignore where appropriate, and periodically inspect the KGML summaries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-graph-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, KGML summaries, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or maintain local JSON knowledge graph files and agent instruction context summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
