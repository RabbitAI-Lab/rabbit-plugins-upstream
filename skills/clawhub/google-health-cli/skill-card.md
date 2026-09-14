## Description:

Google Health is a read-only CLI skill that helps agents authenticate with Google Health, inspect supported health data types, retrieve raw data points and daily rollups, parse exercise sessions, and emit JSON for downstream processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stozo04](https://clawhub.ai/user/stozo04)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and automation agents use this skill to read consented Google Health data through a local CLI and return structured JSON for analysis or workflow automation. It is intended for read-only data extraction, daily health rollups, exercise-session parsing, and carefully scoped API reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health, profile, settings, and account data can be emitted to stdout and then logged, retained, summarized, or forwarded by an agent or pipeline.

Mitigation: Run the skill only in trusted contexts, request the narrowest useful time window and data types, prefer typed commands over broad API reads, and avoid persisting or forwarding output beyond the task.

Risk: OAuth client secrets and cached access tokens are local plaintext credentials, and the configurable API base URL can redirect requests if set to an untrusted endpoint.

Mitigation: Keep config.json and token.json private, avoid shared directories and logs, rotate credentials if exposed, and set GOOGLE_HEALTH_BASE_URL only for endpoints the operator fully trusts.

Risk: The requested Google Health OAuth scopes and consent screen may grant access to more read-only data than a specific task needs.

Mitigation: Review the Google consent screen before approving login, confirm scopes are expected, and operate only against accounts whose owners have knowingly consented to the downstream handling of their data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stozo04/skills/google-health-cli)
- [Source Homepage](https://github.com/stozo04/google-health-cli)
- [Release Downloads](https://github.com/stozo04/google-health-cli/releases)
- [OAuth Setup](OAUTH_SETUP.md)
- [Machine Contract](docs/MACHINE_CONTRACT.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands; CLI data responses are JSON on stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Data-emitting commands keep machine-readable JSON on stdout and send notices, counts, hints, and errors to stderr.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
