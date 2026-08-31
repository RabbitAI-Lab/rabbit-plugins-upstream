## Description:

Turn a written census schedule into one census notice voice clip per labeled cue, delivering a labeled pack of schedule-based audio clips without inventing census outcomes or personal data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External offices use this skill to convert an already written census schedule into a labeled set of notice-time, document, visit-window, and follow-up voice clips. It plans the slot list first, then can create approved Beatra speech or staff-voice clone tasks without inventing census outcomes, penalties, personal records, or eligibility findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad Beatra account connection and stores a shared Device Token locally.

Mitigation: Review the authorization scope before installation, keep the token only in ~/.beatra/credentials.json, and use the bundled uninstall flow or Beatra Console revocation when disconnecting.

Risk: Approved clone and speech stages can spend Beatra credits.

Mitigation: Require the six-field approval card, live price lookup, and one opaque client_request_id per paid request; do not retry billable work with changed arguments.

Risk: Silent package self-updates are enabled by default.

Mitigation: Disable automatic checks with scripts/mcp_client.py update --auto off when local review is required, and use the bundled update check command for explicit review.

## Reference(s):

- [Census notice voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra skill homepage](https://beatra.ai/skills/census-notice-voice)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/census-notice-voice)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans a labeled list of 8 to 20 census notice clips and may return Beatra task IDs, audio artifact details, duration, size, and net charged credits after approved speech generation.]

## Skill Version(s):

0.1.1 (source: manifest.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
