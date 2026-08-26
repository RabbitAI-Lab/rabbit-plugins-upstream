## Description:

Netlify API integration with managed OAuth for viewing sites, deploys, builds, DNS zones, environment variables, and related Netlify administration state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify account, site, deploy, build, DNS, environment variable, webhook, form, and function data through Maton, and to prepare write operations only after resource-specific confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide Netlify administration actions that affect live sites, DNS records, environment variables, webhooks, or production builds.

Mitigation: Default to read-only calls, identify the exact account and resource first, and require explicit confirmation before any create, update, trigger, or delete action.

Risk: OAuth or API access can grant broad Netlify account visibility and administrative reach.

Mitigation: Review OAuth scopes, prefer read-only access where possible, use only the needed Maton connection, and revoke unused connections.

Risk: Ambiguous account or connection selection can route an operation to the wrong Netlify account.

Mitigation: Specify the intended connection and account for account-specific calls before preparing or executing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Maton Homepage](https://maton.ai)
- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and valid Netlify connection context for account-specific calls.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
