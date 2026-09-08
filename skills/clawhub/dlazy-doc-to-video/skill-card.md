## Description:

Converts documents such as Word, Markdown, PDF, PPT, and Excel files into explainer, report, courseware, or training video workflows through the dLazy CLI and its hosted file-to-video template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn uploaded documents into narrated explainer videos, report broadcasts, courseware, or training content while continuing work across dLazy projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the third-party dLazy npm CLI and hosted service, including API access and file upload behavior.

Mitigation: Install only when the dLazy CLI and service are trusted; prefer npx or a non-admin install when avoiding a persistent global binary.

Risk: Documents attached through the CLI are uploaded to dLazy media storage for processing.

Mitigation: Attach only files intended for dLazy processing and avoid sending sensitive documents unless that use is approved.

Risk: The dLazy API key grants access to the user's dLazy organization.

Mitigation: Store the key with user-scoped permissions and rotate or revoke it from the dLazy dashboard when access should change.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project identifiers, uploaded files, and dLazy CLI authentication state.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
