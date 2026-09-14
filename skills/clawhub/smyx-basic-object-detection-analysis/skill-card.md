## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels in target areas from images or video streams for general security surveillance scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run object detection on security images or video streams and retrieve structured reports or cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can process surveillance images or video and query cloud report history using automatic account identity.

Mitigation: Use it only where media upload and history access are authorized, and require documented consent, retention, and access controls before sensitive surveillance use.

Risk: The security review notes plaintext HTTP development endpoints and cloud service calls.

Mitigation: Use a production HTTPS-only configuration and block HTTP endpoints before handling real surveillance media or report links.

Risk: The security review notes reusable tokens may be stored in plaintext shared workspace storage.

Mitigation: Move tokens to a managed secret store or environment-scoped credential mechanism, restrict workspace file permissions, and rotate any exposed tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown or JSON analysis reports, with optional saved text output and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; local media files are limited to 10 MB.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
