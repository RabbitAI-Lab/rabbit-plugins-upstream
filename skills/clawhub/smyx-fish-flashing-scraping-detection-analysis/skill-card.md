## Description:

Analyzes fixed-camera aquarium video to detect fish flashing or scraping behavior, count friction events per minute, and produce ectoparasite-risk warnings with observation guidance rather than diagnosis or treatment instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarists, aquarium operators, and aquaculture teams use this skill to analyze fixed-camera fish video files or URLs for abnormal rubbing behavior. It generates structured warning reports and can retrieve cloud-hosted historical warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded aquarium videos or URLs may be sent to a backend service and history reports may be fetched from the cloud.

Mitigation: Use only footage approved for external processing and confirm consent, retention, and deletion controls before deployment.

Risk: The security scan reports silent identity reuse, local token storage, and unsafe or overbroad network paths.

Mitigation: Review identity and token handling before installation; avoid private footage, production accounts, or real tokens until authenticated requests are restricted to approved HTTPS origins.

Risk: Behavioral warnings could be mistaken for veterinary diagnosis or treatment direction.

Mitigation: Keep outputs limited to ectoparasite-risk warning and observation guidance, and route diagnosis, microscopy, medication, dosage, and treatment decisions to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include tank identifiers, event timestamps, flashing and scraping frequencies, affected fish counts, alert level, recommended observation actions, disclaimers, and report links when available.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
