## Description:

Turn a written visitor reception script into one visitor reception voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External front desk, facilities, and operations teams use this skill to turn an already-written visitor reception script into a labeled set of greeting, check-in, escort, policy, and farewell voice clips. The skill supports catalog voices and authorized staff voice clones while keeping one cue per clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad shared Beatra device authorization for media, artifact, wallet, voice, and task capabilities.

Mitigation: Install only when those account powers are acceptable, keep the device token private, and use Beatra Console revocation or the bundled uninstall workflow when the shared device credential should be removed.

Risk: Silent package updates are enabled by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` after installation when manual update control is required.

Risk: Clone and speech generation can spend Beatra credits and may create duplicate paid work if retried incorrectly.

Mitigation: Show a separate confirmation card for each paid stage, submit each request once with an opaque `client_request_id`, and recover uncertain responses only with byte-identical arguments.

Risk: Staff voice cloning can misuse likeness rights if a local audio file is treated as consent.

Mitigation: Clone only when the user provides voice and likeness rights for an authorized sample, and upload local samples only through the bundled client before calling the clone tool.

Risk: Generated reception clips can misstate visitor facts or policies if the agent invents lines beyond the supplied script.

Mitigation: Use only the provided reception script, stop for missing pronunciations, and review clip content against the script and pronunciation table before delivery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/visitor-desk-voice)
- [Beatra skill homepage](https://beatra.ai/skills/visitor-desk-voice)
- [Visitor desk voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with labeled slot lists, command snippets, JSON payloads, task IDs, billing details, and audio artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 visitor reception voice clip results when live Beatra generation succeeds; clone and speech stages require separate user confirmation.]

## Skill Version(s):

0.1.1 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
