## Description:

Combines facial-feature analysis with physiological indicators to provide stroke-risk screening reports, warnings, lifestyle suggestions, and medical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users provide facial images or videos and optional physiological indicators to receive a structured stroke-risk screening report, warnings, and general lifestyle or care guidance. Users can also request a list of their historical screening reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared-account handling can mix users’ private health reports.

Mitigation: Wait for identity-isolation fixes before using private health media on shared bots; require clear authorization for cloud uploads, protect credentials, and understand retention and deletion terms.

Risk: An option labeled “export only” can still trigger media uploads.

Mitigation: Treat export-only as an upload until this behavior is fixed; require clear authorization before sending sensitive media and review the remote service’s privacy, access controls, and retention practices.

Risk: Screening guidance could be mistaken for a medical diagnosis.

Mitigation: Treat results as screening prompts only; seek professional medical care for high-risk findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON screening reports, Markdown report lists, and text warnings and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, screening scores, high-risk factors, warnings, recommendations, and report links. Screening output is not a medical diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
