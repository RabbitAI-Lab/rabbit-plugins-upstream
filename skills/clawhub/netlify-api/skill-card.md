## Description:

Netlify API integration with managed OAuth for viewing sites, deploys, builds, DNS zones, environment variables, and related Netlify account resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect Netlify account, site, deploy, build, DNS, webhook, form, function, and environment variable state through Maton-managed OAuth. It can also propose administrative Netlify changes, but write operations require explicit user approval with specific resource identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw Maton API passthrough can reach any Netlify endpoint authorized by the connected account, including endpoints outside the documented intended surface.

Mitigation: Use read-only list or retrieve calls first, constrain actions to the documented task, and require explicit approval before any POST, PUT, PATCH, or DELETE request.

Risk: Netlify DNS, environment variable, deployment, deletion, and webhook changes can affect live sites or downstream automation.

Mitigation: Confirm the exact account, connection, resource identifiers, payload, and expected impact before approving high-impact changes.

Risk: Long-lived API keys and returned provider credentials can leak through logs, shell history, command arguments, or persisted files.

Mitigation: Prefer OAuth, avoid printing or storing credentials, keep API keys out of command lines and files, and rotate any key that was exposed.

## Reference(s):

- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/netlify-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Netlify API request paths, CLI invocations, SDK snippets, and approval prompts for write operations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
