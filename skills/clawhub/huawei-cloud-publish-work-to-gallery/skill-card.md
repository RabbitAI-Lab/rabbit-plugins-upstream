## Description:

Publishes a user's project to the Huawei Cloud University Operations Platform work gallery or training camp using scripted checks, packaging, and publish API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and students use this skill to prepare, validate, package, and submit a project to the Huawei Cloud University Operations Platform gallery or an eligible training camp. It guides project selection, STS credential setup, cover and detail asset generation, camp selection, and final publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Huawei Cloud credentials and creates short-lived STS credentials for publishing.

Mitigation: Use a disposable development environment where practical, rely on temporary STS credentials, avoid sharing permanent AK/SK values, and delete temporary STS credential files after publishing.

Risk: The skill may expose a local project through a DevBridge tunnel.

Mitigation: Only tunnel the intended local project, verify the local page before publishing, and close the tunnel after the release workflow finishes.

Risk: The security review flagged unsafe remote installer recommendations for user review.

Mitigation: Verify any remote installer source before running it and prefer documented local setup steps when possible.

## Reference(s):

- [Publish Work to Gallery workflow](SKILL.md)
- [API Specification - Gallery Platform](references/api-spec.md)
- [Work Preparation Guide](references/work-preparation.md)
- [Troubleshooting - Publish Work to Gallery](references/troubleshooting.md)
- [Error Codes - Gallery Platform API](references/error-codes.md)
- [SELF_VERIFY STS publishing flow](references/self-verify-publish.md)
- [DevBridge tunnel notes](references/devbridge-tunnel.md)
- [CodeArts Sandbox publishing](references/codearts-sandbox.md)
- [Windows setup](references/windows-setup.md)
- [Linux work preparation](references/work-preparation-linux.md)
- [Windows work preparation](references/work-preparation-windows.md)
- [Mock Server + Screenshot Template](references/mock-server-template.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, generated image and zip files, and JSON API parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary STS credential files, cover images, screenshots, detail zip packages, and publishing parameter JSON during execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
