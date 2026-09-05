## Description:

Turns a user-supplied public trading calendar and authorized stills into short talking calendar clips, with planning, consent, billing, speech, video, and delivery guidance for Beatra media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External advisors, educators, and supporting agents use this skill to turn already-public trading calendar facts and authorized stills or voice samples into planned, consented, short Beatra talking clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra Device Token grants broad media-generation, voice, artifact, task, and wallet-spend authority.

Mitigation: Review the requested authority before installing, keep the token only in the private credential file, and revoke or uninstall the connection when it is no longer needed.

Risk: Automatic package updates are enabled by default and may replace package-owned files without a separate prompt.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review is required; update code verifies Beatra discovery data, archive checksums, manifest entries, and package-owned destinations.

Risk: Paid clone, speech, and video tasks can spend credits, and uncertain retries can duplicate work if request identity is changed.

Mitigation: Show a live pricing and approval card for each paid stage, submit each approved task once with an opaque `client_request_id`, and retry only byte-identical arguments with the same request identity.

Risk: Voice cloning or talking-head video can misuse likenesses, voices, or non-public calendar claims.

Mitigation: Use only authorized media and voice samples, treat file access as insufficient consent, and speak only dates and session facts supplied from an already-public trading calendar.

## Reference(s):

- [Calendar talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra package homepage](https://beatra.ai/skills/market-calendar-talking)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/market-calendar-talking)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON payloads and shell command examples; generated media is returned as Beatra task artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a visible slot list before paid requests; each approved still maps to one 2 to 15 second talking clip unless the spoken line must be split into separate segments.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
