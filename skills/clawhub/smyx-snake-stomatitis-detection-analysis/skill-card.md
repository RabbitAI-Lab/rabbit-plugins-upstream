## Description:

Analyzes clear snake mouth images or videos to identify visual signs such as mucosa color changes, pus points, ulcers, necrotic tissue, and a low, moderate, or high stomatitis risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, veterinary staff, and developers can use this skill to analyze snake mouth media, produce structured oral-health risk reports, and retrieve prior cloud-hosted reports. The output is visual risk assessment guidance, not a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Snake mouth images, videos, and report history may be processed by the configured lifeemergence.com cloud service.

Mitigation: Use only media appropriate for that cloud service, avoid sensitive files unless the provider is trusted, and confirm retention and deletion practices before production use.

Risk: The skill can create or reuse a local account identity and store remote authentication tokens in the workspace.

Mitigation: Test in a separate workspace or account, review token storage before installation, and request explicit controls from the publisher for production deployments.

Risk: The skill provides visual health-risk assessment for a veterinary condition and could be misused as diagnosis or treatment advice.

Mitigation: Keep outputs limited to visual findings and non-prescriptive guidance, and direct users to a qualified reptile veterinarian for diagnosis, treatment, medication, or procedures.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report text with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual findings, risk level, non-prescriptive recommended actions, disclaimers, and report links.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
