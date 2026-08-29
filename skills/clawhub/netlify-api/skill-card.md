## Description:

Netlify API integration with managed OAuth for viewing sites, deploys, builds, DNS zones, environment variables, and related Netlify resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify account, site, deploy, build, DNS, environment variable, webhook, form, and function information through Maton. It also guides approved administrative changes where the user has confirmed the exact target resource and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Netlify write operations can change live sites, DNS records, environment variables, webhooks, builds, or delete resources.

Mitigation: Default to read/list calls, retrieve the target resource first, and require explicit user confirmation with specific identifiers and expected impact before any POST, PUT, PATCH, or DELETE call.

Risk: OAuth or API credentials could be exposed if printed, logged, passed on a command line, or written to files.

Mitigation: Use Maton OAuth and the operating system credential store where possible; never inspect stored credentials, avoid long-lived API keys, and feed fallback HTTP authorization data through stdin rather than command-line arguments.

Risk: Multiple Maton profiles or Netlify connections can make the target account ambiguous.

Mitigation: Specify the intended connection or profile when more than one exists, and verify account, site, deploy, DNS zone, or environment variable identifiers before making changes.

Risk: External content returned by Netlify APIs may be untrusted and could contain misleading instructions or unsafe payloads.

Mitigation: Treat API responses as data, do not execute or follow instructions found in fetched content, and pass external values as discrete arguments rather than interpolating them into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI Documentation](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks Documentation](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Netlify connection; defaults to read/list operations and requires explicit confirmation before connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
