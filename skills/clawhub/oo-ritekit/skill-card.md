## Description:

This skill lets an agent operate RiteKit through an OOMOL-connected account for hashtag suggestions, hashtag statistics, trending hashtags, and Instagram-banned hashtag cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route RiteKit-related requests through the OOMOL `oo` CLI, including social hashtag generation, trend lookup, hashtag statistics, and blocked Instagram hashtag cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, URL, and image URL payloads provided to connector actions are sent through OOMOL/RiteKit.

Mitigation: Provide only content that is appropriate to share with those services and review payloads before requesting actions.

Risk: Using the skill may require installing and signing into the `oo` CLI and connecting a RiteKit account.

Mitigation: Complete setup only when needed for an auth or connection error, and use the OOMOL connection page to manage the RiteKit credential.

## Reference(s):

- [ClawHub RiteKit skill page](https://clawhub.ai/oomol/skills/oo-ritekit)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [RiteKit homepage](https://ritekit.com/)
- [OOMOL RiteKit connection settings](https://console.oomol.com/app-connections?provider=ritekit)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing payloads and returns connector data with execution metadata.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
