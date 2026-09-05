## Description:

Turn a user-supplied fund dividend announcement and authorized stills into one fund dividend talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and fund marketers use this skill to create short dividend announcement talking clips from user-supplied fund dividend announcements and authorized still images. It helps an agent plan, confirm, generate, and report one clip per still while keeping spoken facts limited to the supplied announcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses broad shared device authorization and persists local credentials.

Mitigation: Install only in environments where this authorization model is acceptable, protect the local Beatra credential files, and uninstall or revoke access when the workflow is no longer needed.

Risk: The workflow can spend wallet credits for voice cloning, speech synthesis, and video generation.

Mitigation: Require explicit approval for each paid stage, use a fresh opaque client_request_id for changed work, and report net charged credits from the completed task.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic update checks with the documented update command in managed or sensitive environments, or review the update behavior before installation.

Risk: Automatic registration telemetry and shared installation state may be unsuitable for some managed environments.

Mitigation: Review organizational policy before installation and avoid deployment where package registration telemetry or shared Beatra state is not allowed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/fund-dividend-talking)
- [Beatra skill homepage](https://beatra.ai/skills/fund-dividend-talking)
- [Dividend talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with JSON payloads, shell command examples, task reports, and generated media file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free slot plan before paid work, then reports task status, output MIME type, duration, size, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
