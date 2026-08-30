## Description:

Brand Jingle Studio helps agents turn a brand name, slogan, and campaign use into original jingle, ad song, and audio-logo candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and brand or marketing teams use this skill to brief, price, confirm, generate, and review commercial brand jingles, audio-logo stings, ad songs, and optional spoken taglines through Beatra media tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a persistent shared Beatra bearer credential that can spend credits and access Beatra media, task, and artifact tools.

Mitigation: Review before installing, keep the credential only in the documented private Beatra credential file, and revoke the Beatra device authorization when it is no longer needed.

Risk: The package silently self-updates local package files by default.

Mitigation: Use the documented update controls to disable silent checks when a fixed local package is required, and review updates before relying on them.

Risk: Paid music and speech generation can be duplicated if an uncertain request is resubmitted with changed arguments or a new request identity.

Mitigation: Confirm paid payloads before submission, use one stable client_request_id per logical request, poll existing tasks for recovery, and create a new request ID only for user-approved changed work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/brand-jingle-studio)
- [Beatra skill homepage](https://beatra.ai/skills/brand-jingle-studio)
- [Brand jingle workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, API calls, Files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, and generated audio artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task status, actual duration, MIME type, size, artifact URL or ID, resolved model, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
