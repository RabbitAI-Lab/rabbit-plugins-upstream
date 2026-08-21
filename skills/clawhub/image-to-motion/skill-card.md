## Description:

Turn a single photo, product image, portrait, illustration, or AI artwork into a short image-to-video clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to animate a supplied still image into a short Beatra image-to-video clip with directed subject motion, camera movement, billing admission, task recovery, and result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad Beatra creative-tool and wallet-spending authority.

Mitigation: Install only if that authority is acceptable; require the prepaid admission card and explicit top-up or sufficient-balance confirmation before any billable video request.

Risk: A shared Beatra device token is stored under ~/.beatra.

Mitigation: Use the bundled authorization flow, keep the credential file private, and do not expose tokens in chat, command arguments, environment variables, logs, backups, or diffs.

Risk: The bundled client may silently self-update local package code before ordinary Beatra commands.

Mitigation: Disable silent update checks with python3 scripts/mcp_client.py update --auto off when automatic replacement is not acceptable; use update --check for manual review.

Risk: The skill sends package, platform, and installation metadata to Beatra.

Mitigation: Review the package before installation and install only when sharing that metadata with Beatra is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/image-to-motion)
- [Beatra skill homepage](https://beatra.ai/skills/image-to-motion)
- [Motion brief, request, and recovery](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with JSON tool payloads, shell commands, and returned video artifact links or task facts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task status, resolved model, dimensions, duration, usage, charged credits, and visible quality review when available.]

## Skill Version(s):

0.1.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
