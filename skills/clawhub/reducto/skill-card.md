## Description:

Reducto document processing API integration with managed API key authentication for parsing, extracting, splitting, and editing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Reducto through Maton, process user-selected documents, extract structured data, inspect jobs, and perform approved document edits. It is suited for document workflows where the user has authorized the Reducto connection and confirmed any write, upload, automation, or new connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents, document URLs, parsed text, and extracted fields are sent to Reducto for processing and may include sensitive business or personal data.

Mitigation: Use the skill only for user-selected documents, prefer explicit uploads over tokenized URLs, summarize or extract only needed fields, and avoid forwarding raw results unless the user approves the destination.

Risk: Connection creation, document uploads, edits, and other write operations can authorize access, consume credits, or change document state.

Mitigation: Require explicit user confirmation for new Reducto connections and every POST, PUT, PATCH, or DELETE operation, including the target resource, payload, and intended effect.

Risk: API keys, destination headers, body templates, and raw HTTP fallback paths can expose long-lived credentials if handled casually.

Mitigation: Prefer OAuth and the Maton CLI credential store, send raw API keys only to api.maton.ai when the CLI cannot be used, never embed credentials in trigger destinations, and rotate any key that was printed, committed, or pasted.

Risk: Hosted functions, triggers, destinations, and event watch --exec can create persistent automation or data forwarding beyond a one-time Reducto API call.

Mitigation: Use hosted automation only when the user asks for it by name, keep destinations on api.maton.ai or *.maton.app unless a third-party host is explicitly approved, deploy reviewed handlers with least privilege, and avoid --exec except for user-reviewed local handlers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/reducto)
- [Maton Homepage](https://maton.ai)
- [Reducto Documentation](https://docs.reducto.ai)
- [Reducto API Reference](https://docs.reducto.ai/api-reference)
- [Reducto Studio](https://studio.reducto.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Reducto API responses or derived summaries when the user has an active Maton connection and approves operations that modify data or create automation.]

## Skill Version(s):

1.2.3 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
