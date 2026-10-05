## Description:

Turns each seller-provided product still into a short, silent product-detail clip using confirmed Instagram Reel composition or written composition notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and their agents use this skill to plan one product-page video per product still, optionally consult a public competitor Reel, and deliver the resulting clips after approving credit-priced work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable device authorization can spend credits and access broader Beatra media tools than this clip workflow.

Mitigation: Review the authorization scope before connecting, approve each paid lookup and generation separately, and revoke the device in the Beatra Console when no longer needed.

Risk: The installed package checks for and applies updates automatically without a separate prompt.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if package changes should require manual review.

Risk: Retrying a billable request after an uncertain response could create duplicate work or charges.

Mitigation: Check the existing task first and retry only with the same request ID and identical arguments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/instagram-reel-to-pdp-clip)
- [Beatra skill homepage](https://beatra.ai/skills/instagram-reel-to-pdp-clip)
- [Product-detail clip workflow](artifact/references/workflow.md)
- [Reel lookup](artifact/references/reel-lookup.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Video files, Guidance]

**Output Format:** [Labeled shot list and task reports in text, with separate generated video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One silent clip per still; Reel lookups and video generation are separate credit-priced tasks.]

## Skill Version(s):

0.1.7 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
