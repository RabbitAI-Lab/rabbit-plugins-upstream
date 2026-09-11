## Description:

Turns written articles or documents into narrated explainer videos by outlining, storyboarding, generating voiceover, building, and validating the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to direct the dLazy CLI to turn pasted articles or attached documents into narrated explainer, training, courseware, or report videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill depends on dLazy's hosted service and npm package.

Mitigation: Review the CLI source and prefer npx or an isolated environment over a global install when possible.

Risk: Authentication requires a dLazy API key that may be stored locally or provided through the environment.

Mitigation: Use a revocable API key and rotate or revoke it from the dLazy dashboard when access should change.

Risk: Files passed with the CLI are uploaded to dLazy storage for processing.

Mitigation: Attach only files intended for upload and review dLazy service terms before processing sensitive content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI status or error text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; attached local files are uploaded to dLazy storage through the CLI.]

## Skill Version(s):

1.0.18 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
