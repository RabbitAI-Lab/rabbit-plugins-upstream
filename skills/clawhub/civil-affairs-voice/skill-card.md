## Description:

Turns a written civil-affairs materials list into 8 to 20 labeled voice clips, with one spoken cue per listed materials item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External and public-sector service teams use this skill to turn existing civil-affairs materials lists into labeled speech-generation plans and audio clips for each cue. It is intended for marriage, birth, household, social-insurance, funeral, disability, veteran, adoption, assistance, and appointment materials-list voice packs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token with broad Beatra account capabilities.

Mitigation: Install only in an environment where broad Beatra account access is acceptable, keep `~/.beatra` private, and avoid exposing the token in chat, command arguments, logs, or environment variables.

Risk: Automatic updates are enabled by default and can replace package files without a separate confirmation.

Mitigation: Disable silent update checks for the installation with `python3 scripts/mcp_client.py update --auto off` when review-controlled package changes are required.

Risk: Speech generation and voice cloning are paid Beatra operations that can create asynchronous tasks.

Mitigation: Show a separate approval card for each paid stage, use opaque `client_request_id` values, and retry uncertain paid calls only with byte-identical arguments.

Risk: Voice cloning can misuse a found or accessible audio file if consent is assumed from file access.

Mitigation: Clone only when the user confirms likeness and voice rights for the sample; otherwise use a catalog voice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/civil-affairs-voice)
- [Beatra skill homepage](https://beatra.ai/skills/civil-affairs-voice)
- [Civil affairs voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 labeled clips and uses the bundled Beatra MCP client for paid speech or clone tasks.]

## Skill Version(s):

0.1.1 (source: server release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
