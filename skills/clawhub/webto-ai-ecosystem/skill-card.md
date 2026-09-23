## Description:

Provides a WebToWork reference skill for agents assisting with AI chat widgets, knowledge-base retrieval, template workflows, PWA sharing, APK packaging, website cloning, AI SEO, translation, analytics, webhooks, memberships, and WeChat Mini Program AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slepoh](https://clawhub.ai/user/slepoh)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to understand WebToWork capabilities and guide safe use of its MCP and REST API workflows. It is most useful when a user asks an agent to configure, publish, package, clone, analyze, or document WebToWork pages, sites, code projects, leads, webhooks, memberships, or marketplace items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP or REST keys can expose account data or permit changes when read-write credentials are used.

Mitigation: Use read-only keys for inspection, reserve read-write keys for trusted clients and intended changes, and rotate or revoke exposed wk_ keys.

Risk: Publishing, deletion, pricing, webhook, membership, and packaging actions can modify public resources or billing-related settings.

Mitigation: Confirm targets, titles, durations, prices, webhook endpoints, and other material parameters before executing write operations.

Risk: Website cloning, generated SEO text, translations, and packaged applications may create inaccurate, incomplete, or rights-sensitive outputs.

Mitigation: Review cloned or generated content, respect source-site rights, and verify final pages or APK behavior before publishing or distributing.

## Reference(s):

- [WebToWork Skill Reference](references/webto-ai-ecosystem.md)
- [WebToWork OpenAPI specification](https://webto.work/api/v1/openapi.json)
- [ClawHub skill page](https://clawhub.ai/slepoh/skills/webto-ai-ecosystem)
- [Publisher profile](https://clawhub.ai/user/slepoh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline examples, API references, and operational instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; agents may propose API or MCP actions but should confirm write operations before execution.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
