## Description:

Analyzes indoor camera video from a local file or URL to detect pet mouth contact with hazardous non-food items and output warning guidance for sustained contact without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home or pet-safety operators use this skill to analyze indoor pet videos for pica-like contact with wires, plastic, socks, tissues, toy fragments, and similar hazards. It returns structured monitoring results, risk indications, intervention guidance, and report links for pet safety workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video inputs and generated reports may be sent to the configured analysis service and associated with a persistent local or remote identity.

Mitigation: Use only videos the user is comfortable sending to that service, and review endpoint configuration, retention practices, and identity-linkage behavior before installing.

Risk: The skill can silently create or reuse identity data and provide cloud-linked history access that users may not expect.

Mitigation: Review the local API key file, local database behavior, and report-history access path before deployment, and disclose this identity handling to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Pet Pica API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit local video files or video URLs to the configured analysis service and may query cloud-linked analysis history for the current identity.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
