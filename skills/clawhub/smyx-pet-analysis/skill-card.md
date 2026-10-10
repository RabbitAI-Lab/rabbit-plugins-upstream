## Description:

Analyzes pet videos from local files or URLs through a cloud service to produce health observations, potential concerns, and a report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use this skill to review cat, dog, or bird videos for potential health concerns and retrieve prior cloud reports. Its observations are not a substitute for veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report history are processed by a cloud service with insufficiently clear consent and retention controls.

Mitigation: Obtain informed consent before uploading media or accessing report history, and confirm the service's retention policy before use.

Risk: The skill silently creates or reuses an account identity and stores authentication tokens in the workspace data directory.

Mitigation: Disclose account linking and token storage to users; restrict access to stored tokens and obtain clear token-removal instructions before routine use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Pet health analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Text with structured results, report links, and Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can optionally be saved to a file; report history is retrieved from the cloud service.]

## Skill Version(s):

999.999.1009 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
