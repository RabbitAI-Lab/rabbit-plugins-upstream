## Description:

Analyzes aquarium camera footage to estimate fish gill-opening rate and report potential breathing abnormalities with suggested follow-up checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, aquaculture staff, and developers use this skill to review fish breathing rates from aquarium footage, inspect alerts, and retrieve past reports. It suggests checks rather than diagnosing disease or controlling aquarium equipment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media and associated account identifiers are sent to LifeEmergence cloud services.

Mitigation: Use only with media and account information you are comfortable sending to that service.

Risk: The skill creates or reuses a local account identity and stores service tokens in the workspace data directory.

Mitigation: Review local identity and token state before use; clear data/smyx-common-claw.db and data/smyx-api-key.txt if you need to reset the association.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)
- [Fish respiratory monitoring API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Breaths-per-minute estimates, alerts, suggested checks, and links to historical reports when available.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
