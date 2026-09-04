## Description:

Netlify API integration with managed OAuth for viewing and administering sites, deploys, builds, DNS zones, environment variables, forms, functions, services, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect Netlify account, site, deploy, build, DNS, environment variable, form, function, service, and webhook state through Maton. It can also guide administrative changes after confirming the target resource, intended effect, and user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad Netlify API authority through a generic passthrough.

Mitigation: Install only when Netlify administration is intended, prefer OAuth, review requested scopes, and default to read/list calls before proposing changes.

Risk: Site, DNS, webhook, build, form, and environment-variable operations can affect live Netlify services.

Mitigation: Require explicit confirmation with specific resource identifiers, payload details, and the intended effect before any create, update, trigger, or delete operation.

Risk: Requests may target the wrong account when more than one Maton or Netlify connection exists.

Mitigation: Specify the intended profile and connection before acting, especially before write operations.

Risk: Using an API key fallback can expose a long-lived credential through environment, logs, or command history.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is unavoidable, do not print or persist it and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Netlify Skill](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI Documentation](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks Documentation](https://docs.netlify.com/configure-builds/build-hooks/)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Netlify connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
