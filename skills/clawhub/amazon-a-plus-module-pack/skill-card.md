## Description:

Turn seller-supplied selling points into one Amazon A+ module still per point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers and their agents use this skill to plan and generate one Amazon A+ Content module still for each seller-confirmed selling point. It supports module planning, Beatra image generation, result review, task recovery, and billing reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad account access beyond a single image workflow.

Mitigation: Install only when the user trusts Beatra for the shared credential, use an account with controlled credit exposure, and revoke the device authorization when the skill is no longer needed.

Risk: The bundled client checks for and installs skill updates silently by default.

Mitigation: Use the documented update command to disable automatic checks before normal use when change control is required, and rely on the package's verified update path for manual updates.

Risk: Selected reference files are uploaded and host, platform, package, and installation metadata may be recorded or sent.

Mitigation: Upload only intended reference media and avoid including sensitive content that is not required for the A+ module task.

Risk: Image generation is billable and account actions can consume Beatra credits.

Mitigation: Confirm the live model price before billable generation, use one opaque request ID per module, and report returned net charged credits from task results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/amazon-a-plus-module-pack)
- [Publisher Profile](https://clawhub.ai/user/beatra-ai)
- [Beatra Skill Homepage](https://beatra.ai/skills/amazon-a-plus-module-pack)
- [A+ Module Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, image artifacts, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples; generated stills are returned as Beatra task artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes module plans, task IDs, resolved models, observed dimensions and formats, and net charged credits when generation succeeds.]

## Skill Version(s):

0.1.2 (source: evidence release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
