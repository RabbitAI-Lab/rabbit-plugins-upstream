## Description:

Turn authorized community event site photos and office-supplied facts into one community site clip per photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting community event offices use this skill to plan and generate one silent 2-15s video clip for each authorized event-site photo, preserving photo order and office-supplied facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected local event photos to Beatra.

Mitigation: Use only authorized photos, inspect each file before upload, and upload through the bundled client instead of passing local paths to remote tools.

Risk: The skill can spend Beatra credits for video generation.

Mitigation: Show the live price, count, and six-field production card before generation, then submit only after explicit user confirmation or top-up.

Risk: The package uses a shared full-scope Beatra device credential.

Mitigation: Install only where the shared account authority is acceptable, keep the credential in the protected local Beatra state directory, and revoke or uninstall through the provided workflow when access should end.

Risk: Automatic updates are silent by default and can replace package-owned files.

Mitigation: Rely on the package's fixed Beatra discovery/CDN paths and checksum verification, and disable automatic checks with the documented update command in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/community-site-clip)
- [Beatra skill homepage](https://beatra.ai/skills/community-site-clip)
- [Community site one-shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks plus Beatra task and artifact summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one silent 2-15s video clip per approved photo and reports actual dimensions, duration, usage, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and bundled manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
