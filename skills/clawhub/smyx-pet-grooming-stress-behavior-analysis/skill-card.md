## Description:

Analyzes pet grooming session videos or video URLs for stress behaviors such as struggling, panting, tail tucking, ear posture, and stress-level signals, returning structured observations for grooming and pet-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet groomers, veterinary clinics, pet care teams, and agents supporting them use this skill to submit grooming videos for stress behavior analysis, receive structured stress-level observations, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote processing of uploaded pet media and history queries may expose sensitive media or report data.

Mitigation: Use only when remote processing is acceptable, disclose that media and report queries are sent to the service, and confirm retention and access controls with the publisher.

Risk: The skill silently creates or reuses remote identities and stores tokens locally.

Mitigation: Require the publisher to disclose identity behavior, avoid silent account creation, and remove or secure local token persistence before deployment.

Risk: Default configuration includes plaintext HTTP endpoints.

Mitigation: Require HTTPS production endpoints and reject private or plaintext defaults before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Pet grooming stress API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report with JSON structured analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stress-level observations, historical report lists, and remote report export links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
