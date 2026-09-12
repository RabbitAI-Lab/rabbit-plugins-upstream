## Description:

Runs a multi-model deliberation across models from different labs via mumo's MCP server, returning full responses plus typed cross-model reactions for architecture decisions, design review, plan review, pressure tests, and contested tradeoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this Hermes Agent skill to ask mumo for independent multi-model review before making high-regret technical or product decisions. It is especially suited to architecture tradeoffs, pre-implementation design review, red-team review, plan review, migrations, auth, security, payments, tokens, and data-exposure decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, snippets, and review context may be sent to mumo and its model-provider panel.

Mitigation: Do not include secrets, credentials, private customer data, or proprietary details unless the organization has approved that data flow.

Risk: Public sharing features can expose deliberation sessions if used carelessly.

Mitigation: Review and redact sessions before sharing them publicly.

Risk: The skill requires a mumo API key for MCP authentication.

Mitigation: Store the key in the Hermes .env file with restricted permissions and reference it from the MCP configuration instead of embedding the credential directly.

Risk: Multi-model deliberation is advisory and can still produce incorrect or misleading recommendations.

Mitigation: Treat panel output as decision support, verify important claims, and test or review changes before acting on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ericatmumo/skills/mumo-hermes)
- [mumo Product](https://mumo.chat)
- [mumo Hermes Install Guide](https://mumo.chat/install/hermes)
- [mumo MCP Reference](https://mumo.chat/docs/mcp)
- [mumo REST API](https://mumo.chat/docs/api)
- [Claim Maps](references/claim-maps.md)
- [Snippet Guidance](references/snippets.md)
- [Model Selection](references/model-selection.md)
- [Synthesis](references/synthesis.md)
- [Takeaway](references/takeaway.md)
- [Operating Notes](references/operating-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown synthesis with optional shell commands, configuration snippets, and MCP tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include claim-map links, typed snippets, round summaries, or follow-up prompts when a deliberation continues.]

## Skill Version(s):

0.6.3 (source: server release evidence, frontmatter, CHANGELOG released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
