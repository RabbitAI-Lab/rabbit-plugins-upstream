## Description:

Turns a written article or document into a narrated explainer video workflow through the dLazy hosted agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to start or continue dLazy projects that turn articles, documents, reports, or course material into narrated explainer videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to the dLazy service for processing.

Mitigation: Use the skill only with content appropriate for dLazy processing, avoid sending secrets or sensitive files unless approved, and review dLazy service terms before use.

Risk: Authentication stores a dLazy API key in the local CLI configuration when using the login flow.

Mitigation: Protect the local config file, prefer the pinned npx command when avoiding a global install, and rotate or revoke the API key from dLazy when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text from dLazy.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The wrapped dLazy template may upload explicitly attached local files and return project-scoped results through the dLazy CLI.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
