## Description: <br>
Knowledge builder that extracts entities, relationships, and key facts from web pages, documents, and files. Builds a searchable knowledge base with entity resolution and auto-summarization. Integrates with memory-router. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to extract entities, relationships, summaries, and source records from web pages, documents, and local files into a searchable local research knowledge base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: URL extraction can make outbound HTTP or HTTPS requests to any user-supplied URL, including private or internal network addresses. <br>
Mitigation: Use only trusted public URLs, avoid private network targets and credential-bearing URLs, and run in a constrained network environment when appropriate. <br>
Risk: Extracted content, summaries, entities, and relationships are stored persistently on disk and may include sensitive information from source material. <br>
Mitigation: Do not use confidential documents, PII-bearing pages, or private sources unless storage is acceptable; review and manually clean memory/research/ after use. <br>


## Reference(s): <br>
- [Research Assistant ClawHub Skill Page](https://clawhub.ai/jlacroix82/skills/agent-researcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON files, shell commands, configuration, guidance] <br>
**Output Format:** [Console text with JSON-backed local knowledge-base files and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persists extracted content, entity indexes, and relationship data under memory/research/ unless RESEARCH_DIR is set.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
