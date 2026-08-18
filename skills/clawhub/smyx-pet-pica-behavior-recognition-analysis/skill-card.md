## Description:

Analyzes indoor pet camera videos or video URLs through a remote service to detect sustained mouth contact with hazardous non-food objects and return non-diagnostic pet safety warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill with indoor camera footage to monitor pets for pica-like chewing or mouthing of wires, plastics, fabric, paper, and similar hazardous objects. It produces safety-monitoring alerts and guidance only; it does not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera videos or video URLs may be sent to a configured remote service.

Mitigation: Install only when this data sharing is acceptable, review the endpoint configuration before use, and avoid submitting sensitive home media.

Risk: The skill can automatically create or reuse an account identity and query cloud report history.

Mitigation: Confirm that automatic identity handling and cloud history lookup fit the intended deployment and account policy before installation.

Risk: Authentication tokens may be stored in a local workspace SQLite database.

Mitigation: Use a trusted workspace, restrict local file access, and clear stored tokens when the skill is no longer needed.

Risk: Packaged configuration may reference development, HTTP, or private-network endpoints.

Mitigation: Review and replace default endpoint configuration with approved production endpoints before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet pica API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance, files]

**Output Format:** [Markdown or JSON structured analysis report with warning guidance and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a file when requested; local video inputs are limited to mp4, avi, and mov files up to 10MB.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
