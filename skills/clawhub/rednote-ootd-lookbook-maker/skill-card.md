## Description:

Create a coordinated REDnote (Xiaohongshu) OOTD lookbook from outfit photos or a styling idea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, stylists, and brand teams use this skill to turn outfit photos or styling ideas into a four-slide REDnote OOTD carousel with image prompts, generation steps, title ideas, caption beats, and tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review labels the release suspicious because it asks users to accept broad shared credentials and media-and-wallet scopes beyond a simple lookbook workflow.

Mitigation: Review the authorization scope before installation, keep the Beatra device token private, and reconnect only when the user explicitly chooses to grant the requested access.

Risk: The package enables silent automatic updates by default.

Mitigation: Disable automatic updates with the documented update command when silent replacement is not acceptable, and rely on the package's checksum and package-boundary checks before accepting updates.

Risk: Image generation and revisions can consume Beatra credits.

Mitigation: Require one clear confirmation that includes the prompt, references, model behavior, count, output relationship, maximum charge, and call count before each paid request.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/rednote-ootd-lookbook-maker)
- [Beatra skill page](https://beatra.ai/skills/rednote-ootd-lookbook-maker)
- [Lookbook planning](references/lookbook-planning.md)
- [REDnote OOTD Lookbook workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces lookbook planning guidance, paid-request confirmations, generated image delivery notes, and post copy; remote image artifacts are returned by Beatra tasks.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
