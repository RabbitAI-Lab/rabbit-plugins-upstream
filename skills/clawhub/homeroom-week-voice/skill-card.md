## Description:

Turn a written homeroom week plan into one homeroom week voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and classroom staff use this skill to turn an existing written homeroom week plan into labeled, forwardable voice clips for daily cues, homework, materials, assemblies, parent notes, and pickup reminders. The agent plans a free slot list first, then uses Beatra speech or voice cloning only after required consent, voice selection, and billing confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Beatra client uses a shared Device Token with broad Beatra account capabilities, not only text-to-speech.

Mitigation: Install only when that access is acceptable, keep ~/.beatra private, and revoke or reconnect the Beatra device if the connection is no longer trusted.

Risk: Silent automatic updates are enabled by default for the installed package.

Mitigation: Review the update behavior and disable automatic checks with the documented update --auto off command when explicit change control is required.

Risk: Uninstall decisions affect shared ~/.beatra connection state used by other Beatra skills.

Mitigation: Use the bundled uninstall script and follow its decision output instead of manually deleting shared credential or registration files.

Risk: Voice cloning and speech generation can incur credits and may involve voice likeness rights.

Mitigation: Collect explicit clone consent, show separate clone and speech billing cards, use fresh request IDs for changed work, and submit paid requests only after user approval.

## Reference(s):

- [Homeroom week voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON and shell command snippets; final user-facing results include labeled slot lists and returned audio artifact details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one labeled clip per scheduled cue, normally 8 to 20 clips, with task polling and billing details reported from Beatra task responses.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
