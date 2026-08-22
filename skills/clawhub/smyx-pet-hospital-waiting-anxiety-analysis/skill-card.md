## Description:

Analyzes pet hospital waiting-area videos or video URLs through server-side APIs to identify anxiety-related behavior signals and return a structured anxiety level from 1 to 5 without diagnosing disease or recommending treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary clinic staff, pet hospital teams, and supporting agents use this skill to analyze waiting-area pet media, identify high-stress animals, and generate structured reports that can inform triage or comfort actions without replacing clinical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet waiting-area media or media URLs are sent to Life Emergence/Open API services for analysis.

Mitigation: Use only media that the clinic or user is authorized to process through those services, and avoid submitting sensitive footage unless that data flow is acceptable.

Risk: The skill can create or reuse an internal identity, store local authentication tokens, and query cloud history reports tied to that identity.

Mitigation: Use a separate workspace or account for sensitive clinic use, and review or clear the local data store before sharing the machine or workspace.

Risk: The anxiety score may be affected by video quality, occlusion, individual pet differences, or breed-specific behavior.

Mitigation: Treat results as waiting-room workflow support only, and combine them with direct observation and veterinary judgment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an anxiety level, observed behavior signals, risk notes, suggestions, report links, and history-report tables.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
