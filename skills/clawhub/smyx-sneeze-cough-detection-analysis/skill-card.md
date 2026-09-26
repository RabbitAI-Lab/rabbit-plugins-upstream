## Description:

Detects sneeze and cough events in pet video, optionally using audio, and returns structured behavior observations, frequency information, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, and animal-care teams use this skill to analyze pet activity videos for sneeze or cough behavior and to review cloud-stored historical reports. The output is intended for behavior observation and triage support, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, optional audio, URLs, report history requests, and account identifiers are sent to the publisher's cloud service.

Mitigation: Use only media you are comfortable sharing with the publisher, and review the publisher's retention, access-control, and identity-handling documentation before use with private household footage.

Risk: The skill can silently create or reuse an identity and store tokens locally.

Mitigation: Run it in a workspace with appropriate access controls and remove locally stored identity or token data when it is no longer needed.

Risk: Detection results may be incomplete or inaccurate and are not medical diagnoses.

Mitigation: Treat outputs as behavior observations; seek veterinary review for frequent, severe, or concerning respiratory events.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [API interface reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown or JSON text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured detection results, event frequency, suggestions, historical report records, and report export links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
