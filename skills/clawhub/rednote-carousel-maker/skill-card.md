## Description:

Create a Xiaohongshu or REDnote carousel from a post outline, product details, photo set, or style reference. Build an ordered 3:4 image sequence with a hook cover and supporting slides, clear focal imagery, matched visual direction, and headline-safe areas for product recommendations, tutorials, food notes, OOTD, travel guides, knowledge posts, and Xiaohongshu content images for one connected post story.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to plan, generate, transform, and refine ordered 3:4 Xiaohongshu/REDnote carousel image sequences with a hook cover and supporting slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent full-scope Beatra device token that can spend credits, upload selected local files, and access media and task tools.

Mitigation: Install and authorize only when those account powers are acceptable; protect the local credential file and disconnect with the bundled uninstall flow when access is no longer needed.

Risk: Billable image generation can consume credits, and accidental changed retries can create new paid work.

Mitigation: Require a final paid-call confirmation, keep the returned task ID, and reuse the same opaque client request ID only for byte-equivalent recovery.

Risk: Automatic package updates are enabled by default and can replace package-owned files without a separate confirmation.

Mitigation: Disable silent checks with `python3 scripts/mcp_client.py update --auto off` when silent replacement is not acceptable; the bundled updater verifies fixed Beatra discovery/CDN paths and package file checksums.

Risk: Reference-based generation may upload selected local image files to Beatra.

Mitigation: Upload only files intended for Beatra processing, preserve the declared order, and avoid exposing credentials or private prompts while handling task recovery.

## Reference(s):

- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/rednote-carousel-maker)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown with tool-call arguments, shell commands, task metadata, and ordered image artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ordered 3:4 image sequences and reports returned dimensions, task ID, resolved model, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
