## Description:

Turn a written civil-affairs materials list into one civil affairs voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External offices and their supporting agents use this skill to turn an existing civil-affairs materials list into labeled spoken instruction clips. It supports free slot planning, optional authorized staff voice cloning, paid speech generation, task polling, and billing reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad Beatra account and spending authority, including speech generation, voice cloning, wallet spending, task access, and artifact access.

Mitigation: Install only when the publisher and authorization scope are acceptable, review the Beatra authorization page before approval, and avoid use on sensitive workstations where local device metadata or generated media access would be inappropriate.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Disable automatic updates for the installation with `python3 scripts/mcp_client.py update --auto off` when change control is required, and use `python3 scripts/mcp_client.py update --check` to inspect available updates.

Risk: The skill stores a shared local Device Token for Beatra access.

Mitigation: Keep `~/.beatra/credentials.json` private, avoid exposing token contents in chat, logs, command arguments, or environment variables, and use the bundled uninstall workflow or Beatra Console revocation when access should end.

Risk: Paid voice clone and speech requests can consume credits, and accidental retries can duplicate work if request identity is not preserved.

Mitigation: Show a cost and work card before each paid stage, use one opaque `client_request_id` per logical request, poll existing tasks before retrying, and retry uncertain submissions only with byte-identical arguments.

## Reference(s):

- [Civil affairs voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/civil-affairs-voice)
- [Beatra skill homepage](https://beatra.ai/skills/civil-affairs-voice)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, task status summaries, and returned audio file artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled slot list before paid work; typical voice packs contain 8 to 20 speech clips and report returned MIME type, duration, size, usage, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: evidence release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
