## Description:

Identifies strangers in surveillance media through facial comparison, supporting video streams and images for stranger warning workflows in residential, workplace, access-control, and similar security settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators and agent users use this skill to analyze uploaded or URL-based surveillance images and videos, compare faces against a known-person base, enroll new faces when requested, and retrieve historical recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, face data, identifiers, and report history may be sent to remote services whose operation and retention practices are under-disclosed.

Mitigation: Verify the configured backend endpoints and operator before installation, document retention and deletion procedures, and avoid private camera footage unless those terms are acceptable.

Risk: The skill can enroll faces and query history under locally managed identity state.

Mitigation: Require explicit consent and authorization for biometric enrollment and history lookup, and confirm how local identity files, SQLite records, and tokens can be deleted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API interface documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown text with structured JSON result blocks and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links, recognition summaries, enrollment results, historical report lists, and local output files when an output path is provided.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
