## Description:

Turns documents, topics, or briefs into narrated explainer videos with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and developers use this skill to invoke the dLazy hosted CLI workflow for converting documents or briefs into explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and executing a third-party CLI can introduce supply-chain and local execution risk.

Mitigation: Review the dLazy CLI source and npm package before installing, and prefer npx or a local/sandboxed install when persistent global installation is not needed.

Risk: The workflow stores or uses a dLazy API key and uploads user-selected files to dLazy services.

Mitigation: Use DLAZY_API_KEY for per-run authentication on shared machines, rotate or revoke stored keys when needed, and upload only documents you are allowed to send to dLazy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-explainer-video)
- [dLazy CLI source and homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash command examples and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate SaaS API calls through the dLazy CLI and may upload user-selected files to dLazy storage.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
