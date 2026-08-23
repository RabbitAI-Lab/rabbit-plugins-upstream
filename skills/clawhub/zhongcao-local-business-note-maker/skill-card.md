## Description:

Create a Xiaohongshu local business post or REDnote local business post from storefront photos, service images, a merchant brief, or brand references, with optional paid Xiaohongshu lookup for platform-grounded research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and local-business operators use this skill to turn business photos, service images, merchant briefs, or brand references into a coordinated three-slide REDnote/Xiaohongshu local-business note plus title ideas, caption beats, fact checks, and tags. Optional paid lookup can read Xiaohongshu notes, comments, or account posts before drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation grants a shared Beatra credential broad paid media permissions.

Mitigation: Review the requested authorization before use, keep the credential file private, and reconnect only when the user explicitly chooses to refresh account access.

Risk: The bundled client self-updates local package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when local review is required before code changes.

Risk: Image generation and Xiaohongshu lookup can spend Beatra credits, and lookup reads are priced per page or operation.

Mitigation: Confirm each paid lookup or generation request separately, quote the current price and maximum charge before execution, and reuse the same request identity only for exact recovery of uncertain submissions.

Risk: Uploaded storefront, service, or brand images are sent to Beatra for processing.

Mitigation: Upload only images the user is comfortable sending to Beatra and keep business claims limited to facts supplied or explicitly looked up.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/zhongcao-local-business-note-maker)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/zhongcao-local-business-note-maker)
- [Local-business note planning](references/local-business-note-planning.md)
- [REDnote Local Business Note workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request payloads, and links to generated image artifacts when paid work completes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a three-slide 3:4 visual-story plan, optional generated image artifacts, title ideas, caption beats, fact checklist, tags, task IDs, and billing facts returned by Beatra.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
