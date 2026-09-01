## Description:

Turn a written customer-onboarding step list into one customer onboard voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Enablement teams use this skill to turn existing customer-onboarding steps into a labeled pack of spoken onboarding clips, with safeguards for pronunciation, voice rights, paid generation, billing, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra authorization that can do more than text-to-speech.

Mitigation: Review the requested Beatra authorization before installing, use a dedicated account or environment when possible, and revoke or uninstall the connection when it is no longer needed.

Risk: Silent package updates are enabled by default.

Mitigation: Consider disabling automatic updates after installation with the bundled update control, and review update behavior before relying on the package in a sensitive workflow.

Risk: Voice cloning and speech generation are paid operations and can create duplicate charges if retried incorrectly.

Mitigation: Confirm each paid stage separately, use a fresh opaque client_request_id for new work, and retry uncertain submissions only with byte-identical arguments and the same request identity.

Risk: A cloned staff voice can create likeness and consent risk.

Mitigation: Use cloning only with an authorized sample and explicit voice rights, and treat file access alone as insufficient consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/cs-onboard-voice)
- [Beatra skill homepage](https://beatra.ai/skills/cs-onboard-voice)
- [Customer onboard voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with labeled clip plans and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate Beatra text-to-speech and voice-clone tasks after explicit confirmation; generated audio artifacts are produced by the remote Beatra service.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
