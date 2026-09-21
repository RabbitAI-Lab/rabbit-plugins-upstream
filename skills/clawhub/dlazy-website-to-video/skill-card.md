## Description:

Turns a website URL into a promotional, social ad, or product demo video by capturing the site, deriving brand cues, storyboarding, adding voiceover, building, and validating the result on a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and agents use this skill to turn a pasted website URL into a promo, social ad, or product demo video through the dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, project context, and files attached with --files may be sent to dLazy as part of the hosted service workflow.

Mitigation: Avoid attaching sensitive files or secrets; use the skill only when sending this data to dLazy is acceptable.

Risk: The dLazy CLI may store an organization API key in local user configuration.

Mitigation: Protect local CLI configuration, prefer npx when avoiding a global install, and rotate or revoke the API key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with CLI commands and streamed dLazy responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project IDs for continuing a session and references to generated video artifacts returned by the dLazy service.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
