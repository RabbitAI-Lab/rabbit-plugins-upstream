## Description:

Wraps the dLazy file-to-video cloud agent to turn blog posts, article links, and supported documents into narrated videos with outlining, storyboard, voiceover, and build steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's file-to-video workflow for converting blog posts, article links, and supported documents into explainer, report, courseware, training, social, or YouTube videos. It is appropriate when the user intends to send prompts and explicitly attached files to dLazy's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised blog-to-video purpose is narrower than the artifact's file-to-video behavior, which can include local file uploads to dLazy cloud endpoints.

Mitigation: Use this skill only when the broader document/file upload behavior is intended, and avoid attaching private or regulated documents unless third-party cloud processing is acceptable.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or passed through the DLAZY_API_KEY environment variable.

Mitigation: Use organization-scoped keys according to dLazy's controls, rotate or revoke keys when needed, and avoid placing keys in prompts, files, or shared logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; attached local files may be uploaded to dLazy cloud endpoints when used.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
