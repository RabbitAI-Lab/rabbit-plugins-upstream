## Description:

Analyzes pet grooming-area images or videos through remote services to estimate coat matting, shed hair volume, grooming effectiveness, and hairball risk, returning a structured care report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet-care users and agent operators use this skill to evaluate grooming results and hairball risk from uploaded pet photos, videos, or URLs, and to retrieve cloud history for prior reports. The output is for pet-care reference, not medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet photos, videos, and submitted URLs are processed by remote lifeemergence.com services.

Mitigation: Use only media and URLs appropriate for that service; avoid private household images or sensitive URLs unless the service's retention and access controls are acceptable.

Risk: The skill creates or reuses cloud-linked identity state and stores account tokens in the workspace data directory.

Mitigation: Run it only in workspaces where persisted identity and tokens are acceptable; clear workspace data or rotate credentials before sharing or decommissioning the environment.

Risk: Hairball and grooming risk outputs are visual care estimates, not veterinary diagnosis.

Mitigation: Treat reports as pet-care guidance and seek qualified veterinary or grooming support for medical concerns, severe matting, or abnormal shedding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links; optional file output when --output is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and history listings; reports are generated through remote lifeemergence.com services.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
