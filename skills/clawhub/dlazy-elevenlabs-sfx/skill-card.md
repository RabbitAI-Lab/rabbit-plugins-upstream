## Description: <br>
Generates 1-22 second sound effects from text prompts using the ElevenLabs text-to-sound model through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and game or audio teams use this skill to generate short foley, ambience, alerts, and game sound effects from text descriptions through a cloud generation API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flagged persistent API-key storage whose promised file-permission protection was not evident in the reviewed CLI package. <br>
Mitigation: Prefer passing DLAZY_API_KEY per invocation on shared machines, or verify the permissions on ~/.dlazy/config.json after login. <br>
Risk: Prompts and supported media paths are sent to the dLazy hosted API and generated outputs are hosted by dLazy media storage. <br>
Mitigation: Avoid sending sensitive prompts or private media unless the user accepts the service and data-handling implications. <br>
Risk: The documented output example uses image/png for a sound-effect skill, and the security guidance treats that example as unreliable. <br>
Mitigation: Validate returned output types, MIME types, and URLs before presenting generated media as final audio output. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [JSON responses and generated media URLs, with shell-command guidance for setup and error recovery.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key and supports prompt, duration, prompt_influence, dry-run, no-wait, and timeout options.] <br>

## Skill Version(s): <br>
1.3.4 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
