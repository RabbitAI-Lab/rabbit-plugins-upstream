## Description:

Turn seller-supplied tender facts into one RFP cover still per project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and procurement-content teams use this skill to turn confirmed project notes into short sets of RFP, bid-file, or tender-document cover stills. It plans the cover list first, then creates one Beatra image-generation task per approved project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with broad media, task, wallet, and artifact scopes.

Mitigation: Install only if those scopes are acceptable, keep the credential in the documented local credential file, do not expose the token in chat, logs, command arguments, or environment variables, and revoke the connected agent from the Beatra Console when access is no longer wanted.

Risk: The bundled client can silently install newer package files during normal use.

Mitigation: Disable automatic updates with the documented update command when reviewed-code stability is required, and use the manual check command before accepting a new release.

Risk: Optional local reference files may be uploaded to Beatra-controlled artifact flows.

Mitigation: Inspect each optional reference before upload, upload only files the user has approved for this task, and avoid sending local paths or unnecessary sensitive content.

Risk: Billable image-generation requests can duplicate charges if transport recovery is handled incorrectly.

Mitigation: Read the live model card before paid work, get approval for the production card, use one opaque client_request_id per project, and retry uncertain submissions only with byte-identical arguments.

Risk: Generated cover text may be wrong, unreadable, or look more official than the seller-confirmed facts support.

Mitigation: Use only seller-confirmed tender lines, do not invent tender numbers, agencies, dates, seals, or faces, and review visible text against the confirmed project note before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/procurement-rfp-cover)
- [RFP cover workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, generated image files, task metadata, and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one image-generation task per approved project and reports returned artifacts, observed dimensions and formats, task IDs, resolved models, and net charged credits.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
