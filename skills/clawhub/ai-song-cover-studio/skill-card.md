## Description:

Turns one accessible reference song recording into a newly interpreted cover with a fresh genre, arrangement, or vocal direction, then reviews the returned result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill to convert an authorized reference recording into one Beatra-generated cover or rearrangement. The workflow covers model preflight, paid-boundary confirmation, task polling, recovery, and post-result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with broad music, artifact, task, wallet, and cancellation scopes.

Mitigation: Install and authorize only in an agent environment you trust; keep the token in the private credential file, do not expose it in chat or command arguments, and revoke the connection from the Beatra Console or bundled uninstall workflow when no longer needed.

Risk: Cover generation consumes Beatra credits and uncertain retries can duplicate paid work.

Mitigation: Confirm the paid boundary before submission, use one stable client_request_id for the frozen payload, retry only the identical payload after transport uncertainty, and report the returned billing.net_charged_credits.

Risk: Automatic updates are enabled by default and may replace package-owned files without separate confirmation.

Mitigation: Review the update posture before installation and run python3 scripts/mcp_client.py update --auto off if silent updates are not acceptable.

Risk: Reference audio may contain copyrighted, private, or unauthorized material.

Mitigation: Upload only audio the user owns or is authorized to use, inspect local media before upload, and avoid promising exact lyric preservation unless the user supplies approved lyrics.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/ai-song-cover-studio)
- [Publisher Profile](https://clawhub.ai/user/beatra-ai)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-song-cover-studio)
- [Beatra MCP Endpoint](https://mcp.beatra.ai/mcp)
- [Song Cover Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local audio, invoke Beatra API calls, submit one paid music-generation task, poll task status, and return audio artifact links plus billing details.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
