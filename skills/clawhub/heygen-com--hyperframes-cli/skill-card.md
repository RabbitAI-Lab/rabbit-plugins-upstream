## Description:

Guides developers through HyperFrames CLI project setup, checks, previews, rendering, publishing, and troubleshooting across local and cloud workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to build and validate HyperFrames compositions, inspect previews, and render or publish videos locally or through managed cloud, AWS Lambda, or Google Cloud Run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floating npx execution can run an unreviewed CLI version.

Mitigation: Prefer a project wrapper or a locked HyperFrames version and review commands before running them.

Risk: Feedback, public issue reports, publishing, and skill installation may send information or change public or local resources.

Mitigation: Review destinations and contents, and obtain explicit approval before sending feedback, filing public issues, publishing, or installing skills.

Risk: Cloud rendering and deployment use HeyGen, AWS, or Google Cloud credentials.

Mitigation: Use least-privilege credentials and review the target cloud operation before execution.

Risk: Prompt-skipping flags can bypass confirmation of consequential operations.

Mitigation: Avoid flags such as --no-confirm unless the user explicitly approves the action.

## Reference(s):

- [HyperFrames CLI release on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)
- [Preview and render guidance](references/preview-render.md)
- [Checks and inspection guidance](references/lint-validate-inspect.md)
- [Hosted cloud rendering guidance](references/cloud.md)
- [AWS Lambda rendering guidance](references/lambda.md)
- [Google Cloud Run rendering guidance](references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create project files, previews, and rendered media when executed.]

## Skill Version(s):

1.0.49 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
