## Description:

LLM Wiki helps an agent incrementally build, maintain, query, and lint a structured cross-linked Markdown knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edde-101](https://clawhub.ai/user/edde-101)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and knowledge workers use this skill to turn a local collection of source material into a persistent Markdown wiki with source summaries, concept pages, cross-links, query support, and lint reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on private notes or documents while maintaining a persistent local wiki.

Mitigation: Confirm the wiki root before init, ingest, lint, Git, or memory actions, and restrict use to content approved for inclusion in the workspace.

Risk: The skill references internet_search for supplemental context, which can expose sensitive query details if used on private material.

Mitigation: Require explicit user approval for each internet_search query before using it with private notes, documents, or wiki content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/edde-101/skills/llm-wiki-2)
- [Server-resolved source provenance](https://github.com/Edde-101/SimpleAgent/tree/main/skills/llm-wiki)
- [Publisher profile](https://clawhub.ai/user/edde-101)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown wiki pages, Markdown lint reports, and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may create or update files inside the selected wiki root and may propose Git or memory actions when appropriate.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
