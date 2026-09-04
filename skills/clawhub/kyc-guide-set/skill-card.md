## Description:

Turn user-supplied account-opening material checklist lines into a four-to-eight still KYC guide set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn already-approved account-opening material checklist lines into a consistent four-to-eight still KYC guide pack, with one still per named material. It is suited for account-opening handouts, guide cards, and checklist visuals where the source requirements are supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses shared Beatra device authorization with broad media, task, artifact, wallet, and voice-related permissions.

Mitigation: Review the requested authorization before use and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented update controls to disable automatic updates when release review is required before new code runs.

Risk: Image generation is billable and transport uncertainty can otherwise cause duplicate or changed work.

Mitigation: Use one opaque request ID per approved still, retry only byte-identical requests with the same ID, and report returned net charged credits.

Risk: Generated KYC guide text can be incomplete, unreadable, or mistaken for official legal guidance.

Mitigation: Review visible printed text against the confirmed pack list and treat unreadable small type as a review item, not as certified legal advice.

## Reference(s):

- [KYC materials guide pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Images, Guidance]

**Output Format:** [Markdown pack lists and confirmation cards with JSON MCP call payloads and generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates one still per named material, normally four to eight stills, with at most two generation tasks in flight.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
