## Description:

Analyzes pet camera or feeder images, videos, local files, and URLs for daily health indicators such as eating, drinking, excretion, mental state, vomiting, and limping, then returns health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and agents use this skill to analyze pet monitoring media and retrieve historical pet health reports. The generated health reports can support routine monitoring but should not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet camera or feeder media, video URLs, report requests, and an internal identity to configured lifeemergence.com services.

Mitigation: Use only with media the user is authorized to share, and ask the publisher for retention, deletion, and authorization details before relying on historical reports.

Risk: The skill stores an account cache containing tokens locally.

Mitigation: Run it in a trusted workspace, restrict access to local cache files, and clear or rotate stored tokens before sharing the environment.

Risk: Health analysis reports may be incomplete or unsuitable for medical decisions.

Mitigation: Treat reports as pet health monitoring references and consult a veterinarian when abnormal behavior or health concerns are detected.

## Reference(s):

- [Pet Health Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown reports and tables, JSON detail output, and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health report links and export URLs returned by the configured service.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
