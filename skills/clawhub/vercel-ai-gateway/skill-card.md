## Description:

Provides Vercel AI Gateway API guidance through Maton for model discovery, pricing and usage checks, account credit inspection, and OpenAI- or Anthropic-shaped inference requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Vercel AI Gateway through Maton: browsing models and provider endpoints, checking prices, credits, and generation usage, and preparing inference requests with explicit approval for billable or modifying actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inference requests can spend credits or bill the connected Vercel AI Gateway account.

Mitigation: Confirm the model, approximate request size, and intent before billable inference, especially for loops, batches, or high token limits.

Risk: Prompts, completions, and provider-routed content may expose sensitive information to gateway observability or upstream providers.

Mitigation: Avoid sending secrets in prompts and treat model output or API-returned content as untrusted data.

Risk: Using the wrong Maton profile or Vercel AI Gateway connection can route requests to an unintended account.

Mitigation: List available connections first and specify the intended connection or profile when multiple accounts are present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/vercel-ai-gateway)
- [Maton homepage](https://maton.ai)
- [Vercel AI Gateway REST API](https://vercel.com/docs/ai-gateway/sdks-and-apis/rest-api)
- [Vercel AI Gateway overview](https://vercel.com/docs/ai-gateway)
- [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models)
- [Vercel AI Gateway models and providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Vercel AI Gateway authentication](https://vercel.com/docs/ai-gateway/authentication-and-byok/authentication)
- [Vercel AI Gateway pricing and credits](https://vercel.com/docs/ai-gateway/pricing)
- [Vercel AI Gateway observability](https://vercel.com/docs/ai-gateway/observability-and-spend/observability)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes OAuth, read/list defaults, explicit approval for new connections and billable inference, and careful handling of credentials and prompts.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
