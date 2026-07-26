## Description: <br>
ElevenLabs Instant Voice Cloning (IVC) uploads a clean voice sample to create a custom voice usable with ElevenLabs text-to-speech. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to invoke the pinned dLazy CLI for ElevenLabs voice cloning from an authorized clean voice sample. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-supplied audio may be uploaded to dLazy-hosted services for processing. <br>
Mitigation: Use only audio that is appropriate to send to dLazy services and review the service terms before using sensitive material. <br>
Risk: Voice cloning can misuse a person's voice if authorization is unclear. <br>
Mitigation: Clone only voices the user is authorized to clone. <br>
Risk: The skill depends on a third-party CLI package and hosted API. <br>
Mitigation: Review the pinned @dlazy/cli package before installation in sensitive environments. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown instructions with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and the pinned @dlazy/cli 1.2.3 package.] <br>

## Skill Version(s): <br>
1.3.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
