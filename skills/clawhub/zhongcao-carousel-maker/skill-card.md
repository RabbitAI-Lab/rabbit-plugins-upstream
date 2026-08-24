## Description:

Create a Xiaohongshu or REDnote carousel from a post outline, product details, photo set, or style reference, building an ordered 3:4 image sequence with a hook cover, supporting slides, clear focal imagery, matched visual direction, and headline-safe areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to plan and generate ordered Xiaohongshu or REDnote carousel image sequences from outlines, product details, photos, or style references. It can optionally read Xiaohongshu notes, comments, or account posts before generation when the user approves the paid lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device credential.

Mitigation: Install only if that credential scope is acceptable, keep the credential file private, and review Beatra account or device revocation options before use.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable silent updates with python3 scripts/mcp_client.py update --auto off, or run python3 scripts/mcp_client.py update --check before accepting an update.

Risk: The skill can upload selected local files and spend Beatra credits after confirmation.

Mitigation: Confirm each paid lookup or generation request separately, review selected files before upload, and avoid providing sensitive local files unless they are required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/zhongcao-carousel-maker)
- [Beatra skill page](https://beatra.ai/skills/zhongcao-carousel-maker)
- [Workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell commands, confirmation text, task metadata, billing details, and ordered image artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces two-to-four-slide 3:4 carousel image sequences through paid Beatra image operations after user confirmation.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
