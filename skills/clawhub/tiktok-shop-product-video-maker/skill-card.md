## Description:

Create TikTok Shop product-video plans from product facts, photos, selling points, and English or Japanese audience context. This AI product video maker produces hooks, a ready-to-film script, shot beats, subtitle cues, localized titles, hashtags, and a product-page-safe CTA for product showcases, demonstrations, unboxings, reviews, and creator-led shopping videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, creators, and commerce teams use this skill to turn merchant-supplied product facts, photos, audience context, and market language needs into a TikTok Shop product-video plan. It helps produce hooks, a ready-to-film script, shot beats, subtitle cues, localized titles, hashtags, a product-page-safe call to action, and a fact checklist before filming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the package carries broad Beatra account authority and stores a shared device token in ~/.beatra.

Mitigation: Install only when that account access is acceptable, keep the token out of logs and chat, and use the bundled uninstall workflow when disconnecting the device.

Risk: The server security summary flags arbitrary remote tool calls, file upload capability, telemetry, and wallet or generation scopes that are broader than product-video planning.

Mitigation: Avoid the generic call and upload commands unless intentionally using remote Beatra tools, and review any JSON tool arguments or local files before submitting them.

Risk: The server security guidance warns that silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with the documented update --auto off command when deterministic review is required, and use update --check before accepting a newer package.

Risk: The artifact workflow warns that unsupported product claims can create marketplace or seller-account risk.

Mitigation: Require merchant-supplied substantiation for product claims, avoid unverifiable superlatives and regulated health or efficacy claims, and keep open questions separate from confirmed facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/tiktok-shop-product-video-maker)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-shop-product-video-maker)
- [TikTok Shop product video workflow](references/workflow.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with product-video planning sections, script lines, shot beats, subtitle cues, localized publishing copy, checklists, and occasional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces planning artifacts only; it does not render video, record narration, upload products, publish ads, or promise sales or platform approval.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
