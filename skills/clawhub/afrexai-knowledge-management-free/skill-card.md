## Description: <br>
Afrexai Knowledge Management Free helps an agent capture unstructured knowledge, structure entities and relationships, query associations, surface relevant context, and manage a local knowledge base lifecycle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators can use this skill to turn meeting notes, technical decisions, project documentation, code context, and natural-language questions into structured knowledge entries, relationship paths, and concise retrieval results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad shell-command authority without explaining why it needs that power. <br>
Mitigation: Install only when shell-command authority is acceptable, and review any proposed command before execution. <br>
Risk: The skill may create or maintain a local knowledge base that could contain sensitive personal or confidential information. <br>
Mitigation: Keep sensitive material out of the knowledge base unless storage location, retention behavior, and deletion or archival steps are understood. <br>
Risk: Outdated, conflicting, or low-confidence knowledge entries could lead to misleading association results. <br>
Mitigation: Preserve source context and confidence values, review conflicts before relying on results, and mark stale or disproven entries as deprecated. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped examples and status/result fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured entities, relationships, source context, confidence values, summaries, execution logs, and error fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
