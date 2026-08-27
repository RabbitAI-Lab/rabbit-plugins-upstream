## Description:

Audits personal or brand sites for AI agent discoverability and helps fix structured data, trust anchor pages, llms.txt, crawlability checks, and Ghost-specific deployment patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and operator agents use this skill to audit and improve personal or brand sites so AI agents can identify the owner, find trust anchors, consume llms.txt guidance, and distinguish fixable gaps from Ghost Pro platform limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require scoped Ghost access that can publish pages or append site header metadata.

Mitigation: Use a dedicated staff account, grant only the access needed for the session, and review the live changes after each step.

Risk: Public-facing trust pages, llms.txt content, or structured data could publish inaccurate identity or contact information.

Mitigation: Require owner approval of exact public copy before publishing and verify the rendered site with the provided checks.

Risk: Ghost code injection changes can overwrite existing analytics, schema, or metadata snippets if handled as replacement writes.

Mitigation: Fetch and read the current injection content first, append new blocks only, and verify the deployed HTML before continuing.

Risk: Ghost API keys or browser-session credentials could be exposed if copied into repositories or handoff specs.

Mitigation: Keep secrets out of committed files and handoffs; pass only non-sensitive implementation context to coding agents.

## Reference(s):

- [Agent Ready on ClawHub](https://clawhub.ai/highnoonoffice/skills/agent-ready)
- [High Noon Office skill homepage](https://github.com/highnoonoffice/hno-skills)
- [Ora Scoring Guide](references/ora-scoring-guide.md)
- [Ghost Deployment Reference](references/ghost-deployment.md)
- [JSON-LD Templates](references/json-ld-templates.md)
- [llms.txt Templates](references/llms-txt-templates.md)
- [Coding Agent Handoffs](references/codex-handoffs.md)
- [Verification Commands](references/verification-commands.md)
- [Ora](https://ora.sh)
- [llmstxt.cloud](https://llmstxt.cloud)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org)
- [web.dev Measure](https://web.dev/measure)
- [AI.txt Format](https://ai-txt.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured handoff blocks, JSON-LD examples, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes gated owner approval, append-only Ghost code injection guidance, post-change verification commands, and coding-agent handoff specs.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
