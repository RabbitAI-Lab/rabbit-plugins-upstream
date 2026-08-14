## Description:

Sync encrypted Apple Health data from an iOS device (iPhone, iPad) to OpenClaw, Hermes Agent, Claude, Codex or any other AI agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lukasosterheider](https://clawhub.ai/user/lukasosterheider)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to pair an iOS Health Sync app with an agent, fetch and decrypt Apple Health snapshots locally, unlink devices, and generate daily, weekly, or monthly summaries on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decrypted Apple Health snapshots, saved summaries, and private sync keys are stored locally under the configured state directory.

Mitigation: Keep the state directory private, avoid sharing backups or reports, and confirm report destinations before saving sensitive output.

Risk: Public onboarding, fetch, and unlink metadata is sent to the listed Supabase relay endpoints.

Mitigation: Run onboarding, fetch, and unlink actions only after explicit user request and confirm that the configured relay endpoints are expected.

Risk: Identity rotation, device unlinking, dependency installation, report saves, and recurring schedules can change local state or ongoing behavior.

Mitigation: Require explicit confirmation for each of those actions, including the exact schedule or output behavior for automation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lukasosterheider/skills/apple-health-sync)
- [Publisher profile](https://clawhub.ai/user/lukasosterheider)
- [Health Sync homepage](https://gethealthsync.app/)
- [iOS app](https://apps.apple.com/app/health-sync-for-openclaw/id6759522298)
- [Config reference](references/config.md)
- [Default configuration](references/configs.defaults.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text guidance with inline shell commands; summaries may be text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local runtime state, Apple Health snapshots, SQLite or NDJSON storage, and saved summaries under confirmed local paths.]

## Skill Version(s):

0.9.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
