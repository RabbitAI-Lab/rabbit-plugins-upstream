## Description: <br>
Dlazy Elevenlabs Dialogue helps an agent invoke the pinned dLazy CLI to generate ElevenLabs eleven_v3 multi-voice dialogue audio from per-line voice assignments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create character dialogue, podcast segments, and short skits by sending dialogue lines, voice IDs, and generation options through the dLazy CLI to a hosted audio-generation service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dialogue text and local files explicitly passed to supported media fields may be sent to dLazy or ElevenLabs infrastructure. <br>
Mitigation: Review user inputs before invocation and avoid sending confidential or restricted content unless the deployment has approved the external service use. <br>
Risk: The dLazy CLI can store an API key in the local user configuration. <br>
Mitigation: Use per-invocation credentials or npx when persistence is not desired, restrict local credential access, and rotate or revoke the key from the dLazy dashboard when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown instructions with bash examples and JSON result envelopes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return hosted generated-output URLs or an async generateId; requires dLazy API credentials.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
