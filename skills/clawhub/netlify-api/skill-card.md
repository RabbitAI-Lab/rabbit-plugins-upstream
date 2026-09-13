## Description:

Netlify API integration with managed OAuth for viewing and administering sites, deploys, builds, DNS zones, environment variables, webhooks, and related Netlify resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify accounts, troubleshoot deploys and builds, and perform approved administrative changes through a managed Netlify connection. It is also used to set up narrowly scoped hosted automation when the user has reviewed the function, trigger, destination, and affected data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted automation can run with broad Maton account authority.

Mitigation: Prefer OAuth and least-privilege Netlify scopes, use a dedicated Maton account for hosted functions when possible, and confirm every write with exact resource identifiers.

Risk: Functions, triggers, destinations, or webhooks can create persistent forwarding or recurring side effects.

Mitigation: Create them only after reviewing the code, destination URL, data fields, persistence, and network policy with the user; keep routine work to direct API calls.

Risk: Netlify data, environment variables, form submissions, or receiver secrets could be exposed through output, logs, or command lines.

Mitigation: Avoid dumping raw sensitive values, do not place provider or Maton credentials in destination headers or body templates, and rotate any receiver secret that was pasted into a command line.

## Reference(s):

- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/netlify-api)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Netlify connection; write operations require explicit user approval with specific resource identifiers.]

## Skill Version(s):

1.2.4 (source: server release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
