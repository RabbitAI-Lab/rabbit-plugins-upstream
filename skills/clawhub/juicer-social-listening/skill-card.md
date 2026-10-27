## Description:

The skill searches recent social posts across multiple networks and summarizes themes, questions, complaints, and notable posts with links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juicer](https://clawhub.ai/user/juicer)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and content creators can use the skill to understand recent public conversations about a topic, find recurring audience questions and complaints, and gather linked quotes and content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to Juicer and could expose confidential topics or identifiers.

Mitigation: Avoid confidential topics and identifiers in searches. Review proposed searches and credit costs before running them.

Risk: Weekly scheduled searches can incur ongoing credit costs.

Mitigation: Agree on the reporting frequency and spending limits before enabling weekly automation.

## Reference(s):

- [Juicer MCP server documentation](https://developers.juicer.io/mcp-server)
- [Juicer developer portal](https://www.juicer.io/developer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown social listening digest with themes, questions, complaints, notable posts, quotes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries reflect recent posts found by best-effort network searches; they are not a complete archive.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
