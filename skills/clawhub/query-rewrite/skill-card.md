## Description: <br>
Rewrites ambiguous or context-dependent retrieval queries into structured search variants for RAG, memory, and wiki search while preserving the original user intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dabin0927](https://clawhub.ai/user/dabin0927) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill before RAG, memory, or wiki retrieval to detect vague, referential, multi-intent, rhetorical, or condition-heavy queries and produce safer search variants alongside the original query. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searching rewritten variants can broaden retrieval beyond the user's original wording. <br>
Mitigation: Use the skill only where expanded retrieval is desired, always include the original query, and deduplicate merged results. <br>
Risk: A rewrite could add unsupported context when a query is ambiguous. <br>
Mitigation: Preserve user intent, avoid rewriting when the query is already clear, and fall back to the original query when the referent or intent cannot be determined. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dabin0927/skills/query-rewrite) <br>
- [Publisher profile](https://clawhub.ai/user/dabin0927) <br>
- [Query rewrite patterns](references/rewrite-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with rewritten query variants, retrieval flow, and fallback handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Keeps the original query in retrieval, can emit 1-N rewritten queries, and caps expanded reference-resolution queries at five items.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
