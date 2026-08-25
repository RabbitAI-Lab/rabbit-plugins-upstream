## Description:

Build a reusable AI character visual pack from one to four ordered reference images or an original character brief, then create character sheets, portraits, full-body poses, expressions, story scenes, and branded mascots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, designers, marketers, comic and game teams, and agents use this skill to plan approved Beatra image requests that establish reusable character anchors and create follow-on poses, expressions, sheets, and scenes. It helps preserve named visual traits while requiring review of returned images for visible drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media and spending scopes.

Mitigation: Install only when comfortable with shared Beatra credential authority, keep the credential in the documented user-only location, approve each paid image request explicitly, and avoid exposing tokens or sensitive prompt content.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with the documented update command when per-update approval is required; the updater verifies discovery data, archive checksums, manifests, and packaged files before replacement.

Risk: Paid image requests can create duplicate work or charges if transport failures are handled incorrectly.

Mitigation: Use one stable client_request_id for the frozen payload, retry only identical uncertain submissions with the same ID, recover lost task IDs through task listing, and treat changed inputs as new approved work.

Risk: Reference-guided image generation may drift from the intended character across outputs.

Mitigation: Separate identity traits from scene changes, preserve ordered reference roles, inspect accessible results against named must-keeps, and report observed drift instead of promising pixel-level consistency.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ip-character-consistency-studio)
- [Beatra skill homepage](https://beatra.ai/skills/ip-character-consistency-studio)
- [Character profile and references](references/character-profile.md)
- [Character-image workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Tasks and results](references/tasks-and-results.md)
- [Bundled MCP client diagnostics](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request details and inline shell commands; optional character-profile JSON or Markdown when the user asks to save a reusable profile.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra artifact references, task identifiers, billing facts, and visible drift observations from completed image tasks.]

## Skill Version(s):

0.1.3 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
