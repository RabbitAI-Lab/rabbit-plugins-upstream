## Description:

PDF.co API integration with managed OAuth for converting, merging, splitting, editing PDFs, and extracting document data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a user-authorized PDF.co connection through Maton for PDF conversion, document assembly, editing, security, barcode, job, and data-extraction tasks. It is also used to configure user-approved Maton functions and triggers around those PDF.co actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents, document URLs, PDF passwords, extracted text, and output links can contain sensitive business data and are processed by PDF.co as a third-party service.

Mitigation: Install and use the skill only when the user trusts Maton and PDF.co for the documents involved; get user approval before submitting non-trivial documents, avoid regulated or highly sensitive files, and never pass internal URLs, token-bearing links, or unneeded PDF passwords.

Risk: Write operations, connection changes, hosted functions, and triggers can modify data or create persistent automation.

Mitigation: Approve each connection, write, function deploy or invocation, trigger, and destination separately; summarize the target resource, payload, destination, data flow, and intended effect before execution.

Risk: Long-lived Maton API keys, trigger destinations, and local event execution can expose credentials or business data if used carelessly.

Mitigation: Use OAuth where possible, keep trigger destinations scoped to specific user-controlled URLs, avoid placing credentials in destination headers or templates, and avoid watch --exec unless the user has reviewed the local script.

## Reference(s):

- [PDF.co API Documentation](https://docs.pdf.co)
- [PDF.co API Reference](https://docs.pdf.co/api-reference)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub PDF.co Skill Page](https://clawhub.ai/byungkyu/skills/pdf-co)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved PDF.co connection.]

## Skill Version(s):

1.2.2 (source: server release metadata; frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
