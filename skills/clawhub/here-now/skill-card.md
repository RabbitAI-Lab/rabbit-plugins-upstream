## Description:

here.now lets agents publish websites and files to live URLs in seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to publish static websites and files, manage site access and team workspaces, and share the resulting live URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can expose unintended private files, and some access tokens lack destination safeguards.

Mitigation: Authorize publication explicitly, upload a clean output folder containing only intended public files, choose access restrictions before publishing, use narrowly scoped Drive tokens with explicit expiry, and pin reviewed installations.

## Reference(s):

- [here.now Documentation](https://here.now/docs)
- [here.now OpenAPI Specification](https://here.now/openapi.json)
- [here.now Skill Release on ClawHub](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Configuration instructions]

**Output Format:** [Published websites and files with live URLs, accompanied by Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The published output depends on the user's files, access settings, and publication options.]

## Skill Version(s):

1.35.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
