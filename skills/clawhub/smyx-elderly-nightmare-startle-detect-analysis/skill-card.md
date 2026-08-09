## Description: <br>
Using a fixed bedroom camera with infrared night vision and microphone audio, the skill analyzes elderly nighttime sleep media to detect sudden sitting up, screams, arm thrashing, and related abnormal sleep events, then records event timing, frequency, and duration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, family members, elderly-care operators, and developers use this skill to analyze night-vision sleep video/audio for behavioral event statistics, timelines, sleep-continuity indicators, and clinician-facing reference summaries. It is intended to support observation and referral decisions, not to provide medical diagnosis or medication guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles highly sensitive bedroom sleep video/audio through provider cloud APIs. <br>
Mitigation: Use only with explicit consent from the person being recorded, confirm cloud data-handling expectations, and avoid sending third-party or internal URLs unless the backend fetch behavior is trusted. <br>
Risk: The skill may retrieve cloud report history and manage a local identity database with stored tokens. <br>
Mitigation: Review local storage, retention, and access controls before deployment, and limit use to environments where stored identity data is acceptable. <br>
Risk: Sleep-event outputs may be mistaken for medical diagnosis. <br>
Mitigation: Present outputs as behavioral observations and referral support only, and keep diagnosis or medication decisions with qualified clinical professionals. <br>


## Reference(s): <br>
- [API Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with event timeline, event counts, risk signal level, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write results to a file when an output path is supplied; history queries return cloud report listings.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
