## Description:

Triggers when a user provides a pet oral snapshot image or video for analysis; it supports local uploads or network URLs, evaluates gum color and tartar coverage, and returns standardized oral health observations to support early awareness without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and pet-care platform operators can submit oral snapshot images or videos to receive structured observations of visible gum color and tartar coverage, or retrieve prior reports. The results support care awareness and do not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be mixed between users, and account creation or saved credentials may not be clearly disclosed.

Mitigation: Require per-user isolation and clear controls for account creation and saved credentials; avoid shared-user deployment until isolation is verified, and keep API credentials separate from user identifiers.

Risk: Submitted media is sent to LifeEmergence services, retention and deletion policies are unverified, and the export-only setting may not prevent uploads.

Mitigation: Disclose media uploads, verify export-only behavior and retention/deletion controls, and avoid submitting sensitive media until those controls are confirmed.

## Reference(s):

- [API interface guide](references/api_doc.md)
- [Usage demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured observations in text or JSON; historical report lists can be presented as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gum color observations, estimated tartar coverage, care guidance, and report links. Not a diagnosis.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
