## Description:

Turns one approved white-background Amazon listing main image into a short product-motion clip for the listing main video slot while preserving the approved pack shot as the first frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketplace operators use this skill to plan and generate one short product-motion clip from an already approved Amazon main image. It guides the agent through image inspection, shot planning, live Beatra model checks, seller approval, billable generation, polling, and delivery review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broad account capabilities.

Mitigation: Review the package before installation, keep the credential private, and use Beatra account access and revocation controls when access is no longer needed.

Risk: The bundled client silently updates package-owned files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when local change control is required.

Risk: Approved local images may be uploaded to Beatra for generation.

Mitigation: Upload only seller-approved images needed for the requested clip and confirm account data-handling expectations before use.

Risk: Generated video frames can drift from the approved pack shot, label text, white background, or planned motion.

Mitigation: Review the delivered clip against the locked shot plan and report drift instead of treating it as faithful output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/amazon-main-image-motion)
- [Beatra package homepage](https://beatra.ai/skills/amazon-main-image-motion)
- [Main image motion workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one approved image to one clip, with a free shot plan before explicit approval for billable Beatra video generation.]

## Skill Version(s):

0.1.2 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
