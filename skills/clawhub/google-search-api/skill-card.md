## Description:

Search Google and get the full structured SERP as JSON, including organic results, ads, knowledge graph, AI overview, related questions, and other current web result features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run current Google searches through Scavio and return structured SERP data for research, fact checking, and source-backed answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and requested search context are sent to Scavio through the Google Search API.

Mitigation: Install and use the skill only when sending those queries to Scavio is acceptable for the intended workflow.

Risk: The skill requires a SCAVIO_API_KEY, and mishandling the key could expose account access.

Mitigation: Store SCAVIO_API_KEY in the agent environment or a secret manager, not in source files or public logs.

Risk: The optional LangChain package increases dependency footprint.

Mitigation: Prefer the direct HTTPS example for minimal dependencies, or install the package in an isolated environment and review package source or hashes where available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-search-api)
- [Scavio Search API Documentation](https://scavio.dev/docs/search-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Scavio Rate Limits Documentation](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples, shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends search queries to the Scavio Google Search API.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
