## Description:

Analyzes facial images or videos for micro-expressions and returns an emotion analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Users seeking a structured facial-expression report can submit an image, video, or media URL for automated micro-expression analysis, or request a list of prior reports. Treat the report as an indicative interpretation rather than a verified account of a person's inner state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media is sent to a remote analysis service; retention, downstream handling, account creation, and charges are unverified.

Mitigation: Confirm the processor's media retention, account requirements, and charges before submitting facial media, and share only media you are authorized to submit.

Risk: Credential handling is unsafe, and identity requests or logs may expose a secret; the no-analysis option may still upload media.

Mitigation: Defer installation until credential handling and the no-analysis option are fixed. Use a separate nonsecret identity, protect token storage, and consider rotating any secret previously used with the skill.

Risk: The accuracy of remote emotion analysis is unverified, so reports may misrepresent a person's emotional state.

Mitigation: Treat results as tentative and do not use them as proof of intent or as a substitute for professional psychological assessment or counseling.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text or JSON analysis reports; Markdown tables for report lists, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion labels, facial-expression cues, suggestions, and report links; interpretation accuracy is unverified.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
