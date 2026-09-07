## Description:

Turn YouTube insurance captions into one talking insurance clip per approved still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth and insurance advisors use this Agent skill to plan and generate a small pack of separate talking clips that read advisor-supplied insurance clause lines against approved still images, optionally using public YouTube captions as source material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared broad Beatra account token.

Mitigation: Install only when that account-level access is acceptable, keep the token out of chat and logs, and revoke or uninstall the connection when it is no longer needed.

Risk: The package can run billable media operations through Beatra.

Mitigation: Review the live price and confirmation card for each lookup, clone, speech, and video stage before approval, and preserve request identities during recovery to avoid duplicate paid submissions.

Risk: Selected local media files can be uploaded to Beatra for generation.

Mitigation: Inspect still images and voice samples first, confirm rights and consent, and upload only approved files through the bundled client.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when change control is required.

## Reference(s):

- [Insurance caption talking-clip workflow](references/workflow.md)
- [YouTube insurance caption lookup](references/caption-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/youtube-insure-caption-talking)
- [Beatra skill homepage](https://beatra.ai/skills/youtube-insure-caption-talking)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON MCP arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid Beatra MCP operations that may return separate audio or video artifacts; clips are not stitched together.]

## Skill Version(s):

0.1.2 (source: evidence.json release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
