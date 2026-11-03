## Description:

Based on computer vision, automatically detects and recognizes cats and dogs appearing in the target area from the perspective of feeder/IPC cameras, and supports pet identity recognition and database entry, suitable for pet identification management in smart feeding scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-feeder operators use the skill to analyze images or videos from feeder or fixed IPC camera views, identify or enroll cats and dogs, and review historical reports. The results can inform feeding decisions and should be confirmed by a person.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can silently register or reuse accounts, save credentials, and upload media, including when `--export-env-only` is selected.

Mitigation: Do not rely on that option to prevent side effects. Require fixes and clear disclosure of remote registration, saved tokens, and credential destinations before use.

Risk: Media is sent to LifeEmergence, and the advertised `--api-url` option does not redirect processing. Server retention, deletion, and account-isolation terms are unverified.

Mitigation: Confirm those data-handling terms before submitting household footage or using a shared workspace; submit only media approved for that service.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface notes](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON reports and Markdown summaries or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include pet detection and identity results, enrollment status, feeding suggestions, and report links. Supported media is limited to files up to 10 MB; a person should confirm results.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
