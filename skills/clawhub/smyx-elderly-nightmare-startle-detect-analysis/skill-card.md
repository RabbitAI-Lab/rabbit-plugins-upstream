## Description:

Analyzes fixed bedroom camera sleep video with audio to identify sudden sitting-up, screams, arm-thrashing, and related nighttime events, producing event timing, frequency, duration, risk signals, and caregiver-facing report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers, elder-care providers, and developers of care-monitoring workflows use this skill to analyze consented nighttime bedroom audio/video for sleep-startle and nightmare-like behavior events. The skill prepares non-diagnostic reports that can support care review or a medical consultation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive bedroom audio/video through cloud services.

Mitigation: Use only with the monitored person's explicit informed consent, confirm the cloud service is approved for the deployment, and prefer privacy-preserving modes such as body outlines and face masking when available.

Risk: The release scanner reports silent account identity handling, local token storage, and account-linked report history.

Mitigation: Restrict access to the workspace data directory, review generated local identity records and stored service tokens before and after use, and rotate or remove credentials when the skill is no longer needed.

Risk: The release scanner reports default private-network development API configuration.

Mitigation: Audit the bundled API configuration before installation and replace any private or development endpoints with the intended production service endpoints.

Risk: Sleep-startle and nightmare-like behavior analysis could be mistaken for a medical diagnosis.

Mitigation: Present outputs as behavioral observations only, avoid medication or diagnosis recommendations, and direct frequent or suspicious patterns to qualified neurology or sleep-clinic review.

Risk: Long-term retention of raw nighttime video would increase privacy exposure.

Mitigation: Avoid retaining raw overnight footage; keep only the minimum event snippets and metrics needed for review, with encryption and access controls.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown or JSON-formatted structured report text with report URLs; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links, historical report listings, event timelines, frequency summaries, and non-diagnostic care guidance.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
