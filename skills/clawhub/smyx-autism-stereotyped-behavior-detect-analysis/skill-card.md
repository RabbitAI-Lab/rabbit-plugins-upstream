## Description:

Analyzes fixed-camera child behavior videos to detect and report repetitive stereotyped behaviors such as spinning, hand flapping, and body rocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Rehabilitation therapists, special-education staff, developers, and caregivers can use this skill to process child behavior videos or URLs and receive objective behavior statistics and report links. The outputs support professional review of intervention progress and are not a diagnosis, rating scale, or rehabilitation prescription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive children’s behavior videos, URLs, account identifiers, and report-history requests may be sent to configured cloud services.

Mitigation: Use only with explicit guardian consent, confirm the service and retention terms, and avoid use where local-only processing is required.

Risk: The skill silently creates or reuses local identities and stores tokens locally.

Mitigation: Run it in a controlled workspace, protect local data and token files, and clear stored credentials when the analysis environment is retired or shared.

Risk: Strict tenant or account separation may be required for sensitive child-health workflows.

Mitigation: Validate account routing and report-history access before deployment, especially in multi-user or shared rehabilitation-center environments.

Risk: Computer-vision behavior classifications can be inaccurate in low-quality, multi-person, or ambiguous videos.

Mitigation: Have qualified caregivers or clinicians review samples and treat outputs as objective behavior statistics rather than clinical diagnosis or prescription.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Analysis API Error Reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown or JSON analysis report with event-level behavior statistics, summaries, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a user-specified output file.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
