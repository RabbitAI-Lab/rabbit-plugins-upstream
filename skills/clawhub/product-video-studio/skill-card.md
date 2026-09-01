## Description:

Turn one product photo into a vertical product video that speaks. This AI product video generator and product video maker builds ecommerce product videos, product ads, and commerce short videos from a single photo \u2014 composing a 9:16 opening frame, writing a short script from what the photo shows and the details you supply, voicing it with a selected narrator, and directing one finished clip ready to post. Use it for product launches, listing videos, shoppable social posts, storefront promos, and turning a phone snap of merchandise into a video that sells, with no shoot, no crew, and no editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and their agents use this skill to turn a product photo plus traceable product details into a short vertical product video with spoken narration for listings, launches, storefront promotions, and social commerce posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra token in ~/.beatra and broad Beatra account scopes can increase blast radius in sensitive environments.

Mitigation: Review before installation, use a dedicated Beatra account where appropriate, and disconnect through the bundled uninstall flow when the package is no longer needed.

Risk: Automatic package updates may replace package files without separate confirmation.

Mitigation: Disable automatic updates with the documented update command in sensitive environments and rely on the package's fixed-source, checksum-verified update controls when updates remain enabled.

Risk: Paid generation can consume credits or create duplicate work if retries are not controlled.

Mitigation: Use the skill's staged confirmations, stable request identifiers, and identical-payload retry rules before each paid Beatra task.

Risk: Unsupported product claims can lead to misleading commerce copy.

Mitigation: Use only visible photo facts or merchant-supplied traceable claims, and keep unsupported effect claims in draft.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/product-video-studio)
- [Beatra skill homepage](https://beatra.ai/skills/product-video-studio)
- [The first frame](references/first-frame.md)
- [Writing the narration](references/copy-craft.md)
- [Commerce video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Media artifacts]

**Output Format:** [Markdown guidance with inline shell commands, JSON tool payloads, and returned media artifact details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one short vertical product video workflow with staged approvals, traceable claims, Beatra task metadata, and billing facts.]

## Skill Version(s):

0.1.4 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
