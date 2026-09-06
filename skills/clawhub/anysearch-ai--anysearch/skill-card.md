## Description:

Real-time search engine supporting web search, vertical domain search, parallel batch search, and URL content extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anysearch-ai](https://clawhub.ai/user/anysearch-ai)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agent users use AnySearch to retrieve current web information, run domain-specific searches, batch independent queries, and extract page content through bundled cross-platform CLI tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the skill can send search queries, extracted URLs, and configured API keys to AnySearch.

Mitigation: Use anonymous mode when practical, avoid sensitive queries, and configure API keys only when the user explicitly accepts the data-sharing behavior.

Risk: The security summary reports uneven consent and warning language around creating third-party accounts and persisting returned API keys in plaintext local files.

Mitigation: Do not allow an agent to register an account with a real email address or write an API key to .env unless the user explicitly approves and understands the key will persist on disk.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/anysearch-ai/skills/anysearch)
- [AnySearch API](https://api.anysearch.com)
- [AnySearch API Keys](https://anysearch.com/console/api-keys)
- [AnySearch Skill Releases](https://github.com/anysearch-ai/anysearch-skill/releases)
- [Interface Specification](scripts/shared/doc_spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and inline shell commands from CLI-backed search, batch search, extraction, and setup workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search queries, extracted URLs, and configured API keys are sent to AnySearch; extract output excludes unsupported binary document and media formats.]

## Skill Version(s):

3.1.1 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
