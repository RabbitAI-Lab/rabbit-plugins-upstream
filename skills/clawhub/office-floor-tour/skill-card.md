## Description:

Turns seller-supplied office floor stills into one office floor tour clip per labeled still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate listing teams and agents use this skill to turn named office-floor stills into one short walkthrough clip per still. The skill first produces a free shot list, then guides confirmed paid Beatra video generation and task recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization that covers multiple media and task tools.

Mitigation: Install only when the user trusts Beatra with that account access, keep the device token in the private credential file, and revoke or uninstall through the documented Beatra workflow when access is no longer wanted.

Risk: The skill can spend Beatra credits by creating paid video generation tasks.

Mitigation: Show the current model, price, request count, and one opaque request identity per still before generation, then submit only after user confirmation and use idempotent recovery to avoid duplicate charges.

Risk: The bundled client stores persistent local installation, registration, and credential state.

Mitigation: Keep the local Beatra state private, never expose tokens in chat or command arguments, and use the bundled uninstall script to decide whether shared connection state can be removed.

Risk: Automatic updates are enabled by default and can replace package-owned files without separate confirmation.

Mitigation: Rely on the documented checksum and package ownership verification, and disable silent checks with scripts/mcp_client.py update --auto off when the user wants manual update control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/office-floor-tour)
- [Beatra skill homepage](https://beatra.ai/skills/office-floor-tour)
- [Office floor tour workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payloads, shell command examples, and returned video artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create one paid Beatra video generation task per labeled still after user confirmation; final video artifacts are returned through Beatra task results.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
