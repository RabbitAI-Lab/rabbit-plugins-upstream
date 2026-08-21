## Description:

Detects cats, dogs, and birds in image or video inputs and returns structured pet monitoring reports for home scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze uploaded pet images, videos, or media URLs for cats, dogs, and birds, then view detection results, counts, confidence-oriented details, report links, or report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and report history are processed through a cloud service and associated with an automatically managed account identity.

Mitigation: Review the service data handling terms before use and disclose the identity association and history retrieval behavior to users.

Risk: The skill can store service tokens and account state in the local workspace.

Mitigation: Run it in a controlled workspace, restrict file access to the data directory, and remove stored tokens when deprovisioning the skill.

Risk: Configuration includes development or private HTTP endpoint defaults.

Mitigation: Use reviewed production HTTPS endpoints and remove private development defaults before general deployment.

Risk: Some bundled API references mention health-analysis endpoints while the release is described as pet detection.

Mitigation: Confirm endpoint purpose and documentation alignment during review so users understand what service receives their media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet detection API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON text returned from cloud pet-detection analysis and history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; history queries are formatted for human reading.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
