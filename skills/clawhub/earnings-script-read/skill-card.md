## Description:

Turn an official earnings script into one spoken earnings script read per labeled section.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and agents use this skill to convert official earnings prepared remarks into labeled speech clip packs, with billing-aware generation and recovery guidance. It is intended for investor-update audio where each labeled section becomes one clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra credential can spend credits and may grant access to more Beatra media tools than this narration workflow requires.

Mitigation: Install only when that account authority is acceptable, review Beatra account permissions, and keep credentials out of prompts, logs, command arguments, and diffs.

Risk: Automatic updates are enabled by default and can replace local package files after verified update checks.

Mitigation: In managed or sensitive environments, disable silent update checks with `python3 scripts/mcp_client.py update --auto off` and run explicit update checks during maintenance windows.

Risk: Uninstalling the last Beatra skill can affect the shared Beatra connection used by other Beatra workflows.

Mitigation: Review whether other Beatra skills rely on the same connection before uninstalling or disconnecting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/earnings-script-read)
- [Beatra skill homepage](https://beatra.ai/skills/earnings-script-read)
- [Earnings script workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 labeled speech clips; generated audio artifacts are created through Beatra tasks outside the card output.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
