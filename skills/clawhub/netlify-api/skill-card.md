## Description:

Helps agents inspect Netlify sites, deploys, builds, DNS, and environment variables through a connected Maton account, with approval required for administrative changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site administrators use this skill to check Netlify site information, deploy status, and build activity, and to request approved changes to sites, DNS, and environment variables. It can also guide explicitly approved hosted functions and event-triggered workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative writes may change or delete Netlify resources.

Mitigation: Obtain explicit approval and verify exact site, account, and resource identifiers before each change.

Risk: Environment variable values, build hook URLs, and credentials may be exposed.

Mitigation: Limit OAuth scopes, do not reveal sensitive values, and keep credentials out of logs and shared output.

Risk: Webhooks, event destinations, hosted functions, and local event handlers can create persistent data flows or unattended actions.

Mitigation: Require separate approval for automation and destinations; review recipients, forwarded fields, and any --exec handler before enabling them.

## Reference(s):

- [Netlify API documentation](https://open-api.netlify.com/)
- [Netlify build hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Netlify skill release](https://clawhub.ai/byungkyu/skills/netlify-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Text or Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Netlify API responses may be JSON; commands require a connected Maton account and network access.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
