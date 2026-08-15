## Description:

Guide a contributor through adding a new service to the catalog by checking URL Onboarding, selecting an admission track, opening an issue, writing the service dossier, updating manifests, and preparing a pull request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoruilee](https://clawhub.ai/user/haoruilee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and catalog maintainers use this skill to evaluate an agent-native service, collect official evidence, open the required issue, draft the service dossier, update catalog indexes, and prepare a pull request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may prepare catalog changes or git commands for the wrong repository, service, or issue if inputs are mistaken.

Mitigation: Confirm the target repository, service URLs, issue approval, file changes, and git push before submission.

Risk: Generated service dossiers can contain inaccurate official evidence or onboarding claims.

Mitigation: Review official sources, verify links, and test URL Onboarding before opening the pull request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haoruilee/skills/add-to-awesome-list)
- [awesome-agent-native-services repository](https://github.com/haoruilee/awesome-agent-native-services)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with issue fields, dossier templates, table rows, and git command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewable catalog contribution text and commands; does not execute hidden actions.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
