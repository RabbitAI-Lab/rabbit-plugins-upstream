## Description:

Searches GitHub repositories, code, and issues; Stack Overflow Q&A; Hacker News discussions; and Hugging Face models, datasets, and Spaces for developer research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to search developer platforms for code examples, open-source projects, issues, technical Q&A, discussions, and Hugging Face resources. It supports agent workflows that need structured search results from public developer APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional GitHub and Hugging Face tokens can be mishandled if broad personal tokens are supplied on the command line or captured in logs.

Mitigation: Use least-privilege tokens through environment variables and avoid placing real credentials in skill payloads, reports, logs, or commits.

Risk: The httpx dependency is declared with a lower bound only, so future dependency changes could affect runtime behavior.

Mitigation: Pin or constrain httpx in the deployment environment before production use.

Risk: Search results come from external public APIs and may be incomplete, rate-limited, unavailable, or misleading.

Mitigation: Treat returned JSON as search evidence, verify important results at the source, and fall back to web search when dependencies or network access fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-code)
- [GitHub Search API](https://api.github.com/search)
- [Stack Exchange advanced search API](https://api.stackexchange.com/2.3/search/advanced)
- [Hacker News Algolia Search API](https://hn.algolia.com/api/v1)
- [Hugging Face Hub API](https://huggingface.co/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scripts emit normalized JSON with success, query, provider, items, and error fields.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
