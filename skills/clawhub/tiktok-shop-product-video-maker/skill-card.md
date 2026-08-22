## Description:

Create TikTok Shop product-video plans from product facts, photos, selling points, and English or Japanese audience context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, merchants, and creators use this skill to turn product facts, product photos, target market context, and selling points into a filmable TikTok Shop product-video plan. It produces hooks, script lines, shot beats, subtitle cues, localized titles, hashtags, a supported call to action, and a fact checklist for merchant review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra device token that is shared across Beatra skills.

Mitigation: Review the authorization before installation, keep the credential file private, and use the bundled uninstall workflow or the Beatra Console to revoke access when it is no longer needed.

Risk: The bundled client can upload local files when its upload command is invoked.

Mitigation: Upload only intended regular files, confirm file contents before upload, and avoid passing sensitive local paths to the client.

Risk: Automatic updates are enabled by default and can replace package-owned files silently.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` where manual change review is required; the bundled updater verifies discovery data, checksums, archive contents, and package-owned destinations.

Risk: Product-video copy can include unsupported advertising, marketplace, comparison, or regulated-category claims if source facts are incomplete.

Mitigation: Require merchant-supplied facts for prices, stock, ratings, certifications, efficacy, comparisons, and regulated-category claims; rewrite unsupported claims and deliver a fact checklist for merchant confirmation.

## Reference(s):

- [Product video workflow](references/workflow.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/tiktok-shop-product-video-maker)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-shop-product-video-maker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with optional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes hook options, a line-by-line script, shot beats, subtitle cues, localized titles, hashtags, a product-page-safe call to action, and a merchant fact checklist.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
