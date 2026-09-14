## Description:

Alerts users to supported Amazon listing field changes, such as titles, bullet points, and images, by comparing saved product snapshots with deterministic diffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to manage ARI Amazon listing snapshot watches and read deterministic watch digests for supported listing-field changes. It is intended for listing change alerts, not real-time monitoring, page modification, sales inference, inventory tracking, order analysis, or true return-rate estimation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key, creating ordinary credential-storage exposure if used from shared or untrusted home directories.

Mitigation: Treat the ARI API key as sensitive, use the skill only from trusted user directories, avoid shared or synced configuration paths, and rotate or remove the key when the skill is no longer used.

Risk: The watch workflow can create, pause, resume, and delete Amazon listing snapshot watches when explicitly requested.

Mitigation: Review the ASIN, marketplace site, schedule, and watch ID before running management commands, and execute only actions the user explicitly requested.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/listing-change)
- [Amazon Listing Change Alert Reference](references/reference.md)
- [Amazon Listing Change Alert Watch Workflow](references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output from the ARI CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and targets the fixed watch/listing workflow with watch_digest output.]

## Skill Version(s):

1.4.11 (source: server evidence, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
