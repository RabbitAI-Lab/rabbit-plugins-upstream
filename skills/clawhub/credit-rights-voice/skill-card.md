## Description:

Turn a written credit-card benefits table into one spoken clip per labeled cue, delivering an 8 to 20 file credit-rights voice pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance desk users use this skill to turn an existing credit-card benefits table into labeled spoken clips while preserving the table's stated benefits and approval boundaries. The skill supports catalog voices or an explicitly authorized cloned staff voice, with user confirmation before paid clone or speech calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account permissions, including wallet-spend and media/tool access.

Mitigation: Use a separate low-privilege Beatra account where practical, review the clone and speech cards before paid calls, and approve only the work the finance desk requested.

Risk: The shared local Device Token could expose Beatra access if copied into logs, chat, command arguments, or other files.

Mitigation: Keep the token only in the documented credentials file with user-only permissions, never print or paste it, and revoke the device when the skill is no longer needed.

Risk: Silent automatic updates can replace package-owned files before ordinary commands.

Mitigation: Disable automatic updates with the documented update setting when manual review is required, then run explicit update checks before accepting a new release.

Risk: Transport uncertainty around paid clone or speech calls can accidentally create duplicate work if requests are replayed with changed inputs.

Mitigation: Recover with the same client_request_id only for byte-identical arguments, use task lookup before replay, and create a new request identity only for user-approved changed work.

## Reference(s):

- [Credit rights voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra credit-rights voice skill page](https://beatra.ai/skills/credit-rights-voice)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Audio files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and generated MP3 audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 labeled clips from user-provided benefits-table rows; paid requests require explicit confirmation and unique client_request_id values.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
