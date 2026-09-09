## Description:

Analyzes post-feeding aquarium or aquaculture video to estimate fish gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarists, aquarium operators, aquaculture teams, and developers use this skill to analyze post-feeding video or URLs, generate structured feeding-activity reports, review history, and surface appetite-decline alerts without diagnosing disease or prescribing treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium video, report history requests, and a stable platform identity may be sent to the Life Emergence service.

Mitigation: Use the skill only with explicit consent for uploads and history lookup, and review data handling expectations before installing.

Risk: The security evidence reports reusable local tokens and insecure development HTTP endpoints.

Mitigation: Do not use packaged development configuration for real data; require HTTPS endpoints and secure token storage or token removal.

Risk: Feeding-activity alerts may be mistaken for a disease diagnosis or treatment recommendation.

Mitigation: Treat outputs as visual activity assessments, avoid medication guidance, and involve an aquatic veterinarian or qualified technician for persistent or severe abnormalities.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown summaries and JSON-style structured analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file and can list cloud-hosted report history.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter: 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
