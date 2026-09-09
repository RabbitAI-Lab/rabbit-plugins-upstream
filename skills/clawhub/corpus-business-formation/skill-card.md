## Description:

Form a US LLC or nonprofit corporation for the user by running the intake yourself through Corpus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakesdev](https://clawhub.ai/user/teakesdev)

### License/Terms of Use:

Apache-2.0

## Use Case:

External users and agents use this skill to collect business-formation details, retrieve current Corpus requirements and pricing, validate intake, and hand the founder a prefilled Corpus link for review and payment. It also supports current US law questions by routing the agent to Corpus law-search tools instead of relying on stale model knowledge.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill delegates workflow control to mutable Corpus-hosted instructions and live service responses.

Mitigation: Install only when routing the workflow through Corpus is acceptable, and prefer a pinned or verified release when available.

Risk: Business and founder details are used to build Corpus handoff links.

Mitigation: Review generated handoff links carefully, avoid sharing them, and do not enter SSNs or payment credentials in chat.

## Reference(s):

- [Corpus Agents Guide](https://corpuslaw.us/agents)
- [Corpus MCP Protocol Reference](https://corpuslaw.us/docs/mcp)
- [Connecting Corpus - exact config per harness](references/harness-setup.md)
- [Agent Skills Specification](https://agentskills.io/specification)
- [ClawHub Skill Page](https://clawhub.ai/teakesdev/skills/corpus-business-formation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline links, tool calls, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Corpus handoff links and harness-specific MCP setup instructions; the agent does not handle payment credentials, file state paperwork, or collect SSNs.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
