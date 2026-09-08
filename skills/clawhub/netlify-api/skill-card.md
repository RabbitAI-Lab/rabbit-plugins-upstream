## Description:

Netlify API integration with managed OAuth for viewing Netlify sites, deploys, builds, DNS zones, and environment variables, with explicit approval required for write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and site administrators use this skill to inspect Netlify account, site, deployment, build, DNS, environment variable, form, function, service, and webhook information through Maton-mediated Netlify API access. It can guide administrative changes only after explicit user approval with specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated Netlify access can expose or change account, site, deploy, DNS, environment variable, webhook, form, and related operational data.

Mitigation: Install only when Netlify administration is intended, review OAuth scopes before authorizing, prefer OAuth over long-lived API keys, and use the least privilege available.

Risk: Ambiguous Maton profiles or Netlify connections can send requests to the wrong account.

Mitigation: Specify the intended profile and connection when multiple accounts exist, and verify account and resource identifiers before making changes.

Risk: DNS, environment variable, deploy, webhook, and deletion operations can affect live websites or remove resources.

Mitigation: Default to read and list operations, then require exact user confirmation with resource identifiers and consequences before any write or deletion.

Risk: Netlify API responses, form submissions, webhook payloads, or logs may contain sensitive or adversarial content.

Mitigation: Treat external content as untrusted data, extract only fields needed for the task, and avoid executing, logging, or persisting returned content unless explicitly required.

## Reference(s):

- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI Documentation](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks Documentation](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Homepage](https://maton.ai)
- [Maton Documentation](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, HTTP request examples, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI or raw HTTP Netlify API requests; write operations require exact user confirmation before execution.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
