## Description:

Chukonu Web Search connects agents to the Chukonu remote MCP search and research tools for web, academic, patent, financial, and China legal/regulatory evidence with structured retrieval assessments and research dossiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hhhwor](https://clawhub.ai/user/hhhwor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and operate a remote MCP search service for current, citeable evidence across web, academic, patent, financial, and China legal/regulatory sources. It is suited for fact checking, counter-evidence search, financial and legal/regulatory retrieval, PDF-oriented research, and multi-turn research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and research questions are sent to a remote MCP service, which may expose confidential legal, financial, business, or other sensitive research topics.

Mitigation: Avoid submitting secrets or sensitive confidential details in queries, and review service/provider trust before using the skill for confidential work.

Risk: OAuth credentials are managed by the MCP host and could be exposed if copied into logs, answers, examples, or manual configuration.

Mitigation: Use the host-managed OAuth flow and do not publish, persist, or manually configure access tokens, refresh tokens, authorization codes, callback URLs, or static Authorization headers.

Risk: Legal, financial, and research evidence can be incomplete, unsupported by filters, stale, partial, or unavailable from a given provider.

Mitigation: Check failures, filter execution, retrieval assessment, source quality, dates, legal status, and research coverage before making claims, and disclose limitations instead of treating retrieval as professional legal or financial advice.

## Reference(s):

- [Chukonu remote MCP endpoint](https://search.houdutech.cn/web/mcp/)
- [ClawHub skill page](https://clawhub.ai/hhhwor/skills/chukonu-web-search)
- [Publisher profile](https://clawhub.ai/user/hhhwor)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with shell command blocks and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve evidence, retrieval assessment, source limitations, and research dossier relationships when answering.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
