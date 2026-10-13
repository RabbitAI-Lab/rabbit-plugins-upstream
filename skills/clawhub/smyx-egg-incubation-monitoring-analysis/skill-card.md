## Description:

Analyzes images or video of incubating turtle and snake eggs to report visible development signals, potential concerns, and monitoring history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile breeders and hobbyists use egg images or video to review incubation progress, identify possible warning signs, and consult past reports. Results are advisory and should not replace a reptile veterinarian's assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Egg images or videos and internal identity values are sent to the publisher's cloud service.

Mitigation: Get informed consent before uploading; confirm the destination, retention and deletion terms, and who can access report history.

Risk: The skill silently creates or reuses persistent account credentials and stores identity and tokens in a local SQLite database.

Mitigation: Disclose account creation before use, limit access to local credential storage, and prefer an explicit opt-in identity flow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [Egg incubation API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown reports and history tables; optional JSON or saved report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include developmental stage, warning signals, suggested actions, and links to past reports.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
