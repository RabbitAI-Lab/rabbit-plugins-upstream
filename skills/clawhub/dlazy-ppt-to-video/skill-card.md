## Description:

PPT 转视频 PPT to Video helps agents use the dLazy file-to-video CLI workflow to turn presentations and other supported documents into narrated explainer, pitch, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to start or continue dLazy file-to-video projects for PPT, PowerPoint, Keynote, and related document inputs. It is used to authenticate with dLazy, attach files when needed, and request generated video outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy API and media storage endpoints.

Mitigation: Use only with documents approved for external SaaS processing, and avoid confidential documents unless the organization approves that upload and API-key storage model.

Risk: The PPT-focused presentation conflicts with broader document-to-video triggers.

Mitigation: Confirm the user intends to process the specific document type before invoking the dLazy workflow.

Risk: The dLazy CLI can save an API key in local user configuration.

Mitigation: Use normal credential hygiene: restrict local config access, prefer approved environments, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream dLazy agent responses in the terminal and may reference generated project state managed by the dLazy service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
