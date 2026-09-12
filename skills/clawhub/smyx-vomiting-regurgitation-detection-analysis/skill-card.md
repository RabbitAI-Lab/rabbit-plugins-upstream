## Description:

AI-powered pet vomiting and regurgitation detection analyzes indoor fixed-camera video to identify vomiting or regurgitation actions, vomitus on the floor, event timing, frequency, and vomitus characteristics for home or veterinary observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, caretakers, and veterinary staff use this skill to analyze indoor pet-area videos for visual signs of vomiting or regurgitation, including action cues, floor vomitus, timing, frequency, and vomitus characteristics. Results are behavior observations only and are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-room footage and report queries may be sent to the publisher's cloud service.

Mitigation: Use only when that data sharing is acceptable, and review the publisher's privacy and retention practices before deployment.

Risk: Default development HTTP configuration can expose private video, account identifiers, and tokens.

Mitigation: Require a production HTTPS configuration and remove cleartext endpoints before normal use.

Risk: Automatic identity handling and local token storage may create account and credential exposure.

Mitigation: Require clear identity/account documentation and secure storage for reusable tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured text with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured analysis reports, historical report lists, risk prompts, suggestions, and report links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter declares 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
