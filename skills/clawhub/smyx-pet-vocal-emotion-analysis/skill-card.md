## Description:

Analyzes cat and dog vocalizations to infer emotions and behavioral intentions such as excitement, anxiety, pain, vigilance, and attention-seeking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use this skill to interpret cat and dog vocalizations and review emotion and behavior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Export-only mode may still upload recordings.

Mitigation: Avoid using it with recordings until fixed; test only with non-sensitive clips in an isolated workspace.

Risk: Credential handling includes credential-as-identity behavior and shared plaintext token storage.

Mitigation: Wait for fixes before using private recordings, and rotate any API secrets that may have appeared in account records or logs.

Risk: Automatic HTTP logging on Windows may expose request details.

Mitigation: Avoid private recordings on Windows until the logging behavior is fixed.

Risk: The --api-url option does not change the service destination, and provider retention has not been independently verified.

Mitigation: Do not rely on --api-url to select a destination; verify the provider's retention policy independently before sending recordings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured analysis report with a text summary and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emotion and behavior labels are estimates; the skill describes results as entertainment and notes that recording clarity affects them.]

## Skill Version(s):

1.0.18 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
