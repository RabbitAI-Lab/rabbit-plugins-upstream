## Description:

Turns a YouTube link or pasted transcript into a Chinese spoken script and remake structure based on the source captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, and agents use this skill to convert user-supplied YouTube captions or pasted transcripts into a Chinese spoken remake script. When requested and confirmed, it can also perform paid public YouTube caption, video, or comment lookups before writing the script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra connection grants a broad shared device token.

Mitigation: Review authorization before installation and revoke the device from the Beatra Console if the connection is no longer trusted or needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a fixed package version is required.

Risk: Public YouTube caption, video, and comment lookups are paid operations.

Mitigation: Confirm each lookup separately, quote the live price returned by `beatra.social.tools.get`, and work from a pasted transcript when no lookup is approved.

Risk: Missing captions or unavailable lookup tools can lead to unsupported script content if the agent guesses.

Mitigation: Use only looked-up captions or user-supplied transcript text, label the source, and state when the transcript is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/youtube-caption-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/youtube-caption-studio)
- [Looking Up Captions](references/caption-lookup.md)
- [Writing the Script](references/script.md)
- [Caption Studio Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client Diagnostics](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Chinese spoken-script sections, remake-structure notes, and inline shell commands when setup or lookup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For paid lookups, reports returned payload facts, task ID, terminal status, and billing.net_charged_credits.]

## Skill Version(s):

0.1.3 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
