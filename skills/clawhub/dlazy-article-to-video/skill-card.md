## Description:

Article to Video turns an article or document into a narrated explainer video workflow using the dLazy CLI and hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to convert articles, documents, reports, courseware, or training material into narrated explainer videos through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and options to dLazy's hosted API.

Mitigation: Install only if hosted dLazy service use is acceptable for the intended data and workflow.

Risk: Attached local files are uploaded to dLazy media storage before use.

Mitigation: Do not attach confidential documents unless the user intends to upload them to dLazy.

Risk: Authentication relies on a dLazy API key stored in local CLI configuration or provided by environment variable.

Mitigation: Rotate or revoke the dLazy API key from the dLazy dashboard when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI invocation and may continue project-scoped sessions.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
