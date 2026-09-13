## Description:

Runs a multi-model deliberation across models from different labs (Claude, GPT, Gemini, Grok, DeepSeek, Kimi, and more) via mumo's MCP server, returning full responses plus typed cross-model reactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use mumo to gather independent model perspectives for architecture decisions, product tradeoffs, design reviews, pre-launch pressure tests, debugging impasses, and security-sensitive changes before committing to an approach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send private code, authentication designs, payment details, customer data, or internal plans to an external multi-model service.

Mitigation: Review prompts before use, redact credentials and regulated data, and avoid sending sensitive material unless the recipient service is approved for that data.

Risk: Claim-map or session links may expose deliberation contents if shared with the wrong audience.

Mitigation: Share session links only with recipients authorized to see the underlying deliberation.

Risk: Panel output is advisory and may introduce incorrect or misleading recommendations into plans or skills.

Mitigation: Treat deliberation results as review input, then verify proposed changes with tests, scans, and human review before deployment.

## Reference(s):

- [mumo product](https://mumo.chat)
- [mumo OpenClaw install guide](https://mumo.chat/install/openclaw)
- [mumo MCP reference](https://mumo.chat/docs/mcp)
- [mumo REST API](https://mumo.chat/docs/api)
- [ClawHub listing](https://clawhub.ai/ericatmumo/mumo)
- [Source repository](https://github.com/mumo-chat/mumo-openclaw)
- [Claim Map Guidance](references/claim-maps.md)
- [Model Selection](references/model-selection.md)
- [Operating Notes](references/operating-notes.md)
- [Snippet Examples](references/snippets.md)
- [Synthesis Guidance](references/synthesis.md)
- [Takeaway Mechanics](references/takeaway.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call instructions, snippets, summaries, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce external MCP tool calls and claim-map or session links when a deliberation is run.]

## Skill Version(s):

0.6.2 (source: server release metadata and changelog, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
