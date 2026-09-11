## Description:

Publishes a user's project or work to the Huawei Cloud University Operations Platform work gallery or training camp submission flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare, validate, package, and publish project work to the Huawei Cloud University Operations Platform gallery or an eligible training camp. It guides project selection, cloud identity setup, cover/detail asset generation, camp selection, and final publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect local project files, Git authentication state, and Huawei Cloud authentication state.

Mitigation: Run it in a dedicated workspace or container and review the requested local and cloud access before execution.

Risk: The workflow handles temporary cloud credentials for publishing.

Mitigation: Use the minimum required temporary STS credentials and delete generated credential files after publishing.

Risk: The workflow can install local browser/font dependencies and may open a public tunnel to a local project.

Mitigation: Review installer commands and destination host settings, expose only the intended local app, and close the tunnel after use.

## Reference(s):

- [API Specification](references/api-spec.md)
- [Work Preparation](references/work-preparation.md)
- [Troubleshooting](references/troubleshooting.md)
- [Self-Verify Publish](references/self-verify-publish.md)
- [DevBridge Tunnel](references/devbridge-tunnel.md)
- [Error Codes](references/error-codes.md)
- [Windows Setup](references/windows-setup.md)
- [Linux Work Preparation](references/work-preparation-linux.md)
- [Windows Work Preparation](references/work-preparation-windows.md)
- [CodeArts Sandbox](references/codearts-sandbox.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown guidance with shell commands, JSON parameters, generated image assets, and packaged files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary STS credential files, cover images, detail ZIP files, screenshots, and gate marker files during the publishing workflow.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
