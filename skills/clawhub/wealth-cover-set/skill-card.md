## Description:

Turn user-supplied session names and themes into a four-to-eight still wealth cover set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan and generate a cohesive pack of investor education session-cover stills from user-supplied session names, themes, language, destination, and optional brand references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with broad media and wallet scopes.

Mitigation: Review the Beatra approval page before authorizing, keep the token in the documented local credential file only, and revoke access from the Beatra Console when the connection is no longer needed.

Risk: The bundled client silently checks for and can install package updates that replace executable package files.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` or run `python3 scripts/mcp_client.py update --check` to review availability before updating.

Risk: Optional local visual references are uploaded to Beatra when used.

Mitigation: Upload only files that are intended to be sent to Beatra and avoid sensitive local files.

Risk: Image generation consumes Beatra credits, and retries can create duplicate paid work if request identity changes.

Mitigation: Confirm the production card before paid calls, use one opaque `client_request_id` per still, and retry only unchanged payloads with the original request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wealth-cover-set)
- [Wealth cover pack workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, pack lists, and generated image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, resolved models, observed dimensions and formats, and net charged credits for generated stills.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
