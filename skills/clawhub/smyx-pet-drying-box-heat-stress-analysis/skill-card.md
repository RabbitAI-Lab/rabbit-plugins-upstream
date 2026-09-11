## Description:

Analyzes pet drying box video files or URLs through server-side APIs to detect early heat stress signals such as open-mouth panting intensity, tongue color, and movement frequency, then returns risk levels, observations, intervention guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet grooming operators, pet hospitals, and developers use this skill to analyze pet drying box videos for early heat stress warning signals and receive structured safety observations. It is intended for drying safety support, not veterinary diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet media and analysis requests to cloud services and persists local identity data for report history.

Mitigation: Install only after confirming the publisher's cloud-processing behavior and accepting the local identity database and token caching model.

Risk: Security evidence reports cleartext development HTTP endpoints for credentials and pet media.

Mitigation: Replace development HTTP endpoints with HTTPS production endpoints before operational use.

Risk: Security evidence reports an install risk from the yaml dependency name.

Mitigation: Correct the dependency to the intended YAML package before packaging or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Pet drying box heat stress API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON structured analysis report with risk observations, intervention recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
