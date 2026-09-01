## Description:

Turns scripts, screenplays, and shot lists into storyboarded, shot-by-shot video projects through the dLazy CLI storyboard workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and production teams use this skill to send a script or scene breakdown to dLazy's storyboard agent and iterate on multi-shot animated video projects with project-scoped context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a dLazy API key saved in local configuration or supplied through an environment variable.

Mitigation: Treat the API key as a credential, restrict local access, and rotate or revoke it if the machine is shared or compromised.

Risk: Messages, parameters, and attached files are sent to dLazy hosted services for processing.

Mitigation: Attach only files that are appropriate to upload to dLazy, and review service terms and organizational data handling requirements before use.

Risk: The skill depends on the third-party @dlazy/cli package and hosted APIs.

Mitigation: Review the dLazy CLI source or npm package before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy CLI project sessions; attached local files may be uploaded to dLazy media storage before use.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
