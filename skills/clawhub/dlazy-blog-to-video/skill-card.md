## Description:

Converts blog posts or article links into narrated videos with storyboards, voiceover, and video assembly through the dLazy CLI and hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy projects that turn blog posts or article text/links into social or YouTube video drafts. The artifact also documents a broader document-to-video workflow for files uploaded through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local files may be sent to dLazy API and media storage endpoints.

Mitigation: Attach only content approved for upload to dLazy and avoid sensitive documents unless the organization has approved that service.

Risk: The skill is broader than its blog-to-video name suggests and may operate as a general file/document-to-video integration.

Mitigation: Review the generated command, selected dLazy template, and attached files before execution to confirm they match the intended workflow.

Risk: API keys and session state are stored locally for reuse by the dLazy CLI.

Mitigation: Authenticate only on trusted machines, protect the local dLazy configuration file, and rotate or revoke organization keys when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with dLazy CLI commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy project IDs, authentication steps, and file-upload commands; generated media is produced by the external dLazy service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
