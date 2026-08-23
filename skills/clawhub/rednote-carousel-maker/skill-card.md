## Description:

Create a Xiaohongshu or REDnote carousel from a post outline, product details, photo set, or style reference. Build an ordered 3:4 image sequence with a hook cover and supporting slides, clear focal imagery, matched visual direction, and headline-safe areas for product recommendations, tutorials, food notes, OOTD, travel guides, knowledge posts, and Xiaohongshu content images for one connected post story.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan, confirm, submit, monitor, and review ordered REDnote/Xiaohongshu carousel image generation requests. It supports outline-based generation, photo/reference composition, and focused slide refinement while preserving slide order, 3:4 canvas intent, billing recovery, and result delivery details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill uses broader Beatra account authority than the carousel purpose requires.

Mitigation: Install only when the user accepts the broad shared Device Token model, keep the token out of conversation and logs, and use the documented uninstall or reconnect flow when access should be removed or changed.

Risk: The skill can initiate paid Beatra image-generation operations under the authorized token.

Mitigation: Confirm the prompt, slide order, canvas, model, controls, and ordered references before each paid request, then reuse the same client_request_id only for byte-equivalent recovery.

Risk: The server security guidance calls out silent package-owned file updates unless automatic updates are disabled.

Mitigation: Use the documented update --auto off command when silent update checks are not acceptable, and rely on the bundled verified update controls for manual checks.

Risk: Generated carousel slides can fail to preserve order, safe text areas, focal clarity, or requested details.

Mitigation: Inspect the returned slide sequence, dimensions, subject consistency, palette, and requested details before delivering links or proposing a focused revision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/rednote-carousel-maker)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-carousel-maker)
- [Workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with shell commands, Beatra task details, and ordered image artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before paid image generation; reports task ID, resolved model, observed dimensions, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
