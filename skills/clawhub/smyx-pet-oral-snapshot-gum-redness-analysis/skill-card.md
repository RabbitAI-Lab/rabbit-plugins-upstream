## Description:

Analyzes pet oral snapshot images or videos through server-side APIs to report visible gum color, redness level, tartar coverage, oral-health observations, and report links without providing a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers of pet cameras, smart pet products, and pet health platforms use this skill to submit local or URL-based pet oral media for oral-health observation reports and cloud history lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet oral media and report-history requests are processed through lifeemergence.com cloud services.

Mitigation: Use non-sensitive media where possible and confirm retention, authorization, and data-handling terms with the publisher before production use.

Risk: Security evidence reports under-disclosed account-linked identity creation, cloud history access, and local token persistence.

Mitigation: Install in a contained workspace or dedicated account, review local identity and token storage, and avoid shared agent accounts unless the publisher clarifies token handling.

Risk: The skill reports oral-health observations that could be mistaken for veterinary diagnosis.

Mitigation: Present outputs as visual care references only and direct users to a veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API error-code documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis reports with report links, plus shell commands for running analysis or listing historical reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file paths or network URLs for pet oral images and videos; documented media size limit is 10 MB.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
