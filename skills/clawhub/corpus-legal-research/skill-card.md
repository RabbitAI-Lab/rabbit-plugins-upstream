## Description:

Helps an agent research current United States law for legality, permits, zoning, licensing, compliance, and filing requirements using live Corpus law search and verbatim citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakesdev](https://clawhub.ai/user/teakesdev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and legal or compliance researchers use this skill to make an agent search current US federal, state, and municipal law before answering legal-status, permit, zoning, licensing, compliance, or filing questions. It is not intended for legal advice, tax-return preparation, courtroom strategy, entity formation, or non-US law.

### Deployment Geography for Use:

Global, for United States legal-research questions.

## Known Risks and Mitigations:

Risk: The optional Hermes plugin install path enables an unpinned external plugin that was not included in the reviewed artifact.

Mitigation: Install the skill directly, or review and pin the exact Hermes plugin version or commit before enabling it.

Risk: Legal research answers can become misleading if the agent relies on memory, snippets, or an uncovered jurisdiction.

Mitigation: Search before answering, read provisions before relying on them, cite returned citations verbatim, and check coverage when jurisdiction support is uncertain.

Risk: Using the skill sends legal-research queries to Corpus.

Mitigation: Use it only when sharing the query with Corpus is acceptable, and do not collect or transmit Social Security Numbers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/teakesdev/skills/corpus-legal-research)
- [Corpus agents guide](https://corpuslaw.us/agents)
- [Corpus MCP protocol reference](https://corpuslaw.us/docs/mcp)
- [Agent Skills specification](https://agentskills.io/specification)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with legal citations and inline shell commands where connector setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Legal research answers should cite returned Corpus citations verbatim and identify jurisdiction; connector setup requires network access to https://corpuslaw.us.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
