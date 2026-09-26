## Description:

Coda API integration with managed OAuth for reading and managing Coda docs, pages, tables, rows, formulas, controls, and permissions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to let an agent inspect and manage Coda documents through Maton with OAuth-scoped Coda access. It supports ordinary API calls and explicitly approved automation for Coda-related workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real changes to Coda documents, including write, delete, and sharing actions.

Mitigation: Confirm the exact target document, resource ID, payload, recipients, and intended effect before any modifying action.

Risk: Functions, triggers, and destinations can create persistent automation or data flow beyond a single API call.

Mitigation: Create automation only when the user explicitly asks for it, review what data will flow and where, and prefer private functions with denied outbound network access unless a specific approved host is required.

Risk: Coda responses and Maton credentials can expose private document content or account access.

Mitigation: Use OAuth where possible, avoid printing or storing credentials, extract only task-relevant response fields, and avoid writing raw API responses to logs or files unless the user asks for that output.

## Reference(s):

- [Coda skill on ClawHub](https://clawhub.ai/byungkyu/skills/coda-api)
- [Maton homepage](https://maton.ai)
- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Coda API Postman Collection](https://www.postman.com/codaio/coda-workspace/collection/0vy7uxn/coda-api)
- [Coda API Python Library](https://codaio.readthedocs.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell, HTTP, JSON, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authenticated Coda connection; write, delete, share, and persistent automation actions require explicit user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
