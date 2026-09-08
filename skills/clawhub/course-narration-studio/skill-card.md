## Description:

Course Narration Studio turns lesson materials into polished narration audio by organizing lessons into speakable scripts, recording a consistent teacher voice, and delivering slide-ready audio for courses and training.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, course teams, training authors, and internal enablement teams use this skill to turn approved lecture text and slide materials into ordered narration packs with a consistent teacher voice. It guides agents through pronunciation planning, optional voice cloning with consent, pilot approval, paid text-to-speech synthesis, task polling, and delivery of labeled lesson audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization for media generation, wallet spending, task access, artifact access, and voice operations.

Mitigation: Install only when the user trusts Beatra with that shared authorization, review the approval page before allowing access, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` after installation when automatic package replacement is not desired, and rely on the documented checksum and rollback controls for manual updates.

Risk: Narrator samples and generated speech can contain sensitive or personally identifiable voice data.

Mitigation: Upload narrator samples only after explicit speaker consent and avoid sending sensitive samples unless the user is comfortable with Beatra's upload and processing flow.

Risk: Paid clone and synthesis requests can create duplicate charges if changed work is retried with the wrong request identity.

Mitigation: Use one frozen `client_request_id` per billable request, retry uncertain submissions only with identical payloads, and create a new request ID only for user-approved changed work.

## Reference(s):

- [Course Narration Studio listing](https://clawhub.ai/beatra-ai/skills/course-narration-studio)
- [Beatra Course Narration Studio homepage](https://beatra.ai/skills/course-narration-studio)
- [Course narration workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, artifact references, durations, usage, and billing credit summaries when the narration workflow is executed.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
