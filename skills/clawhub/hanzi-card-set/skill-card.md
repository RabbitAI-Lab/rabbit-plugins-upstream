## Description:

Turn user-supplied character lists into a four-to-eight still hanzi card set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and educators use this skill to plan and generate a consistent set of hanzi recognition-card stills from characters and supporting text they already supplied. The skill is intended for flashcards, classroom handouts, boards, and screen-ready character card packs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a reusable shared Beatra device token and connects to remote Beatra services.

Mitigation: Install only in an environment where the Beatra account permissions are acceptable, keep the credential file private, and use the bundled uninstall flow when removing the package.

Risk: Generation may spend Beatra credits and billing can settle against measured usage.

Mitigation: Require explicit approval before billable calls, read live model pricing, submit each still once with a unique request ID, and report returned net charged credits.

Risk: User-selected files and installation metadata may be sent to Beatra.

Mitigation: Upload only files the user has deliberately supplied for the task and avoid installing where that telemetry or remote processing is unacceptable.

Risk: The bundled client can silently update package files by default.

Mitigation: Review the automatic update behavior before installation and disable automatic checks with the documented update setting when silent updates are not acceptable.

Risk: The remote MCP connection exposes broad Beatra tool access through the shared credential.

Mitigation: Use the skill only through its bundled client, avoid exposing the bearer token in logs or chat, and review account scope before authorizing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hanzi-card-set)
- [Beatra skill homepage](https://beatra.ai/skills/hanzi-card-set)
- [Hanzi-card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pack plans, generation confirmations, task status summaries, billing summaries, and delivery guidance for generated still files.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
