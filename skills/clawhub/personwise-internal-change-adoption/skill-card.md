## Description:

Builds a grounded interactive digital-human course that helps employees adopt a specific internal change using approved source materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and change teams use this skill to turn approved communications for a reorganization, process change, or software rollout into a private interactive course for employees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update a local CLI and open browser OAuth.

Mitigation: Require explicit approval for install or update actions, use the market-bound PersonWise CLI and service, and never request or handle passwords, tokens, cookies, or secrets.

Risk: The skill can upload user-selected source documents to create a course.

Mitigation: Upload only files named, attached, or explicitly selected by the user; disclose and request approval before uploading any agent-discovered local file.

Risk: Course creation can consume existing PersonWise course credits.

Mitigation: Check account readiness before creating each course, do not buy credits automatically, and stop when the service reports a blocking credit or limit condition.

Risk: Publishing or broader access can expose generated course content.

Mitigation: Default courses to private access and change access, publish, or submit to Topics only when requested and supported by fresh service state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-internal-change-adoption)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)
- [PersonWise service](https://personwise.ai)
- [Signed service descriptor](artifact/assets/service-descriptor.signed.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates an interactive digital-human course through the PersonWise CLI and reports secret-free run, course, source, review, access, and URL details.]

## Skill Version(s):

2.1.9 (source: server release metadata and SKILL.md attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
