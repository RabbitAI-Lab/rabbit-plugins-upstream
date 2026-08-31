## Description:

Analyzes in-cabin DMS video or images to estimate driver head pose and report head-down or side-view distraction events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and fleet-safety operators use this skill to analyze driver-facing DMS camera media, identify head-down or side-view distraction events, and receive structured reports, warnings, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing DMS media can contain sensitive biometric and workplace monitoring data and may be uploaded for cloud processing.

Mitigation: Use only with informed driver or employee consent, confirm the configured API destination before execution, and avoid uploading media that is outside the approved monitoring purpose.

Risk: The skill can create or reuse cloud identity state, query report history, and store identity or token data in the workspace data directory.

Mitigation: Run it in a controlled workspace, review local data retention requirements, and clear stored credentials or history when the deployment no longer needs them.

Risk: Head-pose estimates may be unreliable with poor camera placement, low frame rate, occlusion, sunglasses, masks, hats, glare, or vehicle vibration.

Mitigation: Require clear DMS footage that meets the documented frame-rate and visibility constraints, and treat alerts as driver-assistance signals rather than sole safety decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [Driver head-pose API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the rendered analysis text to a caller-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
