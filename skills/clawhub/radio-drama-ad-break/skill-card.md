## Description:

Turn written radio-drama ad-break lines into one spoken bumper clip per labeled slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External producers and agents use this skill to turn supplied radio-drama sponsor, pre-roll, post-roll, and bumper copy into labeled spoken bumper clips. It helps plan the bumper list, confirm pronunciation and voice rights, and submit Beatra speech or clone work with billing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device authorization is broad and can spend wallet credits while granting access to media capabilities beyond speech.

Mitigation: Install only after reviewing the requested scopes and use the documented Beatra authorization, billing, and uninstall flows to reconnect, revoke, or remove access when needed.

Risk: The bundled client stores a bearer token under ~/.beatra.

Mitigation: Keep the local Beatra state private, never copy tokens into chat, command arguments, logs, diffs, or other files, and rely on the bundled scripts for authorization and disconnection.

Risk: Silent package update checks are enabled by default and can replace package-owned files after verification.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` to disable automatic checks for the installation, or use `update --check` to review the available version before updating.

Risk: Speech and clone operations are paid asynchronous tasks and retries can duplicate work if request identity changes.

Mitigation: Show live pricing before paid stages, use one opaque `client_request_id` per logical request, retry uncertain delivery only with byte-identical arguments, and poll the returned task for authoritative billing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/radio-drama-ad-break)
- [Beatra Skill Homepage](https://beatra.ai/skills/radio-drama-ad-break)
- [Radio-drama bumper workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, audio files]

**Output Format:** [Markdown guidance with JSON request payloads, shell command examples, and generated MP3 bumper clips returned by Beatra tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 labeled bumper clips by default and uses one Beatra speech synthesis request per slot.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
