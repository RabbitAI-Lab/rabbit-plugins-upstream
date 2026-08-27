## Description:

Identifies visible plant leaf disease features from images or videos and returns likely disease types, confidence, general prevention guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, home gardeners, and farm inspectors use this skill to triage plant leaf images or videos for common disease symptoms and retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or URLs submitted for analysis may be processed by an external cloud service and associated with an automatically managed identity.

Mitigation: Use only media that is acceptable for external processing, avoid sensitive location or business data in uploads, and disclose this processing path to users before deployment.

Risk: The skill may create or reuse local identity state and service tokens for report history retrieval.

Mitigation: Run it in an isolated workspace, review local state before installation and after use, and remove stored identity or token files when they are no longer needed.

Risk: The authoritative scanner verdict is suspicious.

Mitigation: Perform security review and scanning before deployment, and deploy only after the cloud processing and local identity behavior are acceptable for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON analysis report with confidence scores, general recommendations, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally write the returned analysis to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
