## Description:

Gildata Data Map helps agents search and read Gildata financial data through OOMOL's oo CLI and an OOMOL-connected Gildata account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect Gildata connector schemas and run financial data queries, stock and fund screening, comparisons, company overviews, news, macro data, and research report searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad dynamic call_tool action may invoke downstream Gildata tools without clear read-only limits.

Mitigation: Review the live schema and effect of each call_tool request or newly discovered downstream tool before execution; run it directly only when its behavior is clearly read-only.

Risk: Using the skill can rely on an OOMOL-connected Gildata account and may require setup, login, connection, or billing steps.

Mitigation: Run setup, login, connection, or billing commands only when the user intentionally wants to connect or maintain that account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gildata)
- [Gildata Data Map Homepage](https://www.gildata.com/products/datamap)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are expected to include JSON data and meta.executionId when actions run.]

## Skill Version(s):

1.0.0 (source: server evidence, release metadata, and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
