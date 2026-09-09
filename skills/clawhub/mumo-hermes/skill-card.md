## Description:

Runs a multi-model deliberation across models from different labs via mumo's MCP server, returning full responses plus typed cross-model reactions for architecture decisions, design and plan review, pre-launch pressure tests, and other high-regret choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical decision makers use this skill to ask a Hermes agent to run a mumo deliberation panel, inspect claim maps and model reactions, and synthesize independent perspectives before committing to risky designs, plans, migrations, launches, or security-sensitive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and included context are sent to mumo and its model panel.

Mitigation: Do not include secrets, credentials, production data, regulated data, or confidential security details unless authorized to share them.

Risk: Shared sessions can expose sensitive prompt or response content.

Mitigation: Use public session sharing only after reviewing and redacting the session contents.

Risk: Panel output is advisory and may contain incorrect or misleading recommendations.

Mitigation: Treat deliberation results as decision support, then verify assumptions, run tests, and apply human review before changing code or operations.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/ericatmumo/skills/mumo-hermes)
- [mumo product](https://mumo.chat)
- [mumo MCP docs](https://mumo.chat/docs/mcp)
- [mumo REST API](https://mumo.chat/docs/api)
- [Hermes install guide](https://mumo.chat/install/hermes)
- [Claim Maps](references/claim-maps.md)
- [Takeaway](references/takeaway.md)
- [Snippets](references/snippets.md)
- [Model Selection](references/model-selection.md)
- [Synthesis](references/synthesis.md)
- [Operating Notes](references/operating-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown synthesis with MCP tool-call guidance and optional YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include claim map URLs, per-round Takeaway summaries, snippet guidance, and next-round steering recommendations.]

## Skill Version(s):

0.6.2 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
