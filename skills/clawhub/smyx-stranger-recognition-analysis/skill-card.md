## Description:

Identifies strangers in surveillance images or video by comparing detected faces with a known-person database and returning structured reports, warnings, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External site operators, access-control teams, and developers use this skill to analyze surveillance images or videos for unknown faces against an enrolled database, enroll known people, and retrieve cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, face data, and report history may be sent to a configured cloud service and associated with an internal identity.

Mitigation: Use only with appropriate authorization and consent; avoid regulated or highly sensitive deployments unless data handling, retention, deletion, and access controls are documented.

Risk: Reusable cloud service tokens may be stored locally for future requests.

Mitigation: Install only in workspaces with protected local storage, restrict workspace access, and rotate credentials when access changes.

Risk: Configured service endpoints should be reviewed before use.

Mitigation: Allowlist expected production endpoints and prefer HTTPS-only configurations before deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and historical report tables.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
