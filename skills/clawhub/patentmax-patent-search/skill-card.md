## Description:

全球专利检索与统计分析 skill for searching patents, looking up specific publications, finding similar patents, analyzing citations, and profiling patent portfolios through the PatentMax/ip930 API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agents use this skill to run patent searches, inspect individual patents, compare similar patents, review citations, and generate lightweight patent landscape or company portfolio analysis. It is intended for evidence-based patent research support, not legal opinions or formal patentability, FTO, or invalidity conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent searches may send patent numbers, technical descriptions, and search strategy details to PatentMax/ip930.

Mitigation: Use the skill only for information you are comfortable sharing with that service, and avoid entering confidential invention details, source code, recipes, or trade secrets unless disclosure is approved.

Risk: A paid PatentMax API key is required and can be exposed if pasted into shared chats, committed files, or command histories.

Mitigation: Store the key in PATENTMAX_API_KEY or a secret store, avoid hard-coding it, and rotate the key if it is exposed.

Risk: The client script supports PATENTMAX_BASE_URL, and a misconfigured or influenced override could send the bearer token to a non-PatentMax host.

Mitigation: Leave PATENTMAX_BASE_URL unset for normal use and set it only when the destination is fully trusted.

Risk: Patent search results, similarity matches, and legal-status snapshots can be incomplete or unsuitable for legal decisions.

Mitigation: Treat outputs as research support, verify important records against official patent-office sources, and consult qualified counsel for patentability, FTO, infringement, invalidity, or licensing decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ip930/skills/patentmax-patent-search)
- [PatentMax API Platform](https://api.ip930.com/features/api-platform)
- [PatentMax API Reference](references/api-reference.md)
- [Installation and Configuration](INSTALL.md)
- [Search Workflow](references/search-workflow.md)
- [Query Syntax](references/query-syntax.md)
- [Query Construction](references/query-construction.md)
- [FAQ](references/faq.md)
- [Pitfalls](references/pitfalls.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; command results are returned as JSON or saved files when the client script is run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PatentMax API key in PATENTMAX_API_KEY and may send patent queries, patent numbers, and technical descriptions to PatentMax/ip930.]

## Skill Version(s):

3.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
