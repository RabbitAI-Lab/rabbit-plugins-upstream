## Description:

Analyzes cat scratch-post videos to estimate scratching frequency, session duration, and intensity, and returns observations on stress and claw health without diagnosing disease or recommending behavior changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and teams operating pet behavior monitoring systems can use this skill to review scratch-post footage and receive standardized observations about scratching frequency, session duration, relative intensity, stress, and claw health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented “do not analyze” option can still submit video.

Mitigation: Confirm the data flow before use and submit only footage and URLs you intend to share with LifeEmergence.

Risk: Automatic sign-in can send credentials as account identity data, and the account reused may not be obvious.

Mitigation: Confirm which account is reused and how identity data is handled before running the skill.

Risk: Cloud media and report retention or deletion practices are not established in the provided evidence.

Mitigation: Confirm retention and deletion practices before uploading footage or requesting reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [Skill introduction and demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Structured JSON analysis or Markdown summary, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intensity is estimated from observed vibration and is relative; camera angle and distance can affect the estimate. Results are observational, not a diagnosis or behavior-correction plan.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
