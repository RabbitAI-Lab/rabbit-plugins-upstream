## Description:

website to video, url to video, landing page to video, link to ad, web promo video — capture the site, derive brand, storyboard, voiceover, build, validate on a Remotion template. Use when the user gives a URL (or just pastes a link) and wants a promo, social ad, or product demo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams and creators can turn a website URL into a promotional, social ad, or product demo video through dLazy’s hosted website-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, and attached files are sent to dLazy; project sessions retain context, and attached files are uploaded to its media storage.

Mitigation: Share only messages, URLs, and files you are comfortable sending to dLazy, and consider existing project context before continuing a session.

Risk: The CLI login flow saves an organization API key in the local CLI configuration, and generation may use paid credits.

Mitigation: Use a trusted device and dLazy account, keep the local configuration protected, and rotate or revoke the key or check credits in the dLazy dashboard when needed.

Risk: The published CLI package and hosted agent have not been audited, according to the security evidence.

Mitigation: Review the CLI package and dLazy service terms before use, especially before installing the CLI or sending sensitive material.

## Reference(s):

- [CLI source code (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Video files]

**Output Format:** [Conversational text and video project outputs from the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local attachments are uploaded to dLazy media storage before use.]

## Skill Version(s):

1.3.37 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
