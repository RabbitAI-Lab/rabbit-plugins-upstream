## Description:

This skill helps an agent use dLazy's website-to-video workflow to turn a website URL into a promotional, social ad, or product demo video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill when they have a website URL and want an agent-assisted workflow for producing a promotional video, social advertisement, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy service.

Mitigation: Use the pinned npx invocation when possible, review the linked CLI source before global installation, and install only when the dLazy service is trusted.

Risk: Requests and attached local files may be sent to dLazy API and file-storage endpoints.

Mitigation: Attach only files intended for upload and avoid sending sensitive inputs unless the user's dLazy account and service terms are acceptable.

Risk: The workflow requires a dLazy API key stored locally or supplied through the environment.

Mitigation: Keep the API key revocable, rotate or revoke it from the dLazy dashboard when needed, and avoid exposing it in prompts, logs, or shared shells.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dLazy project identifiers, prompts for continuing a project, and guidance about uploaded reference files.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
