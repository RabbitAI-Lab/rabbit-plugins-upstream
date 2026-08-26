## Description:

Manages an Obsidian-based LLM Wiki by initializing project structure, ingesting source material into durable wiki pages, answering wiki-grounded queries, and running wiki health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, teams, and developers use this skill to maintain a domain-organized personal or team knowledge base in Obsidian. It helps compile raw sources into linked wiki pages, preserve contradictions and source details, answer questions from the wiki, and lint domain/index health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify an Obsidian wiki during initialization, ingestion, query logging, and lint follow-up work.

Mitigation: Confirm the vault or project path and review the planned file writes before allowing the agent to make changes.

Risk: Broad activation wording may trigger the skill for general wiki or knowledge-base requests.

Mitigation: Use the skill only when the intended target is the specific Obsidian-based LLM Wiki, and clarify intent when a request is ambiguous.

Risk: The skill may mirror the source language when creating or updating wiki pages.

Mitigation: State a preferred output language up front when source-language mirroring is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mebusw/skills/llm-wiki)
- [Source Repository](https://github.com/mebusw/llm-wiki)
- [Karpathy LLM Wiki Note](https://x.com/karpathy/status/1793562750870294638)
- [dragonfly-llmwiki Domain Index Reference](https://github.com/lchrennew/dragonfly-llmwiki/blob/master/AGENTS.md)
- [Ingest Workflow Reference](references/ingest-logic.md)
- [Scenario Templates Reference](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with wiki page content, YAML frontmatter, JSON metadata, file plans, and setup commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write or update Obsidian wiki files through required companion skills when the user confirms the target vault and planned changes.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
