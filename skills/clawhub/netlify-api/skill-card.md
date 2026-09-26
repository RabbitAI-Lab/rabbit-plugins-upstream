## Description:

Netlify API integration with managed OAuth for viewing sites, deploys, builds, DNS zones, environment variables, and webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify account resources, review deploy and build state, and perform explicitly approved administrative actions through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer Netlify resources including DNS, environment variables, webhooks, triggers, hosted functions, build hooks, deploys, and deletes.

Mitigation: Prefer read-only calls first, review OAuth scopes, verify specific resource identifiers, and require explicit user confirmation before any write or destructive operation.

Risk: Netlify responses and trigger payloads may contain sensitive business data or untrusted external content.

Mitigation: Use only the fields needed for the task, avoid logging raw responses unnecessarily, and treat returned content as data rather than instructions.

Risk: Automation through hosted functions or triggers can create persistent side effects after the initial setup.

Mitigation: Require user-authored or user-reviewed handlers, separate approval for creation or invocation, least-privilege connection review, and restrictive network policy where applicable.

## Reference(s):

- [Netlify API Documentation](https://open-api.netlify.com/)
- [Netlify CLI](https://docs.netlify.com/cli/get-started/)
- [Netlify Build Hooks](https://docs.netlify.com/configure-builds/build-hooks/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Netlify connection.]

## Skill Version(s):

1.2.5 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
