## Description: <br>
ElevenLabs music_v1 generates 10-300 second original music from a natural-language prompt for background music, ads, and short-video soundtracks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to invoke the dLazy ElevenLabs music generator from an agent workflow and receive generated media URLs or asynchronous task identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and explicitly referenced media files are sent to the dLazy hosted service and generated outputs are hosted on files.dlazy.com. <br>
Mitigation: Use only prompts and media appropriate for third-party cloud processing, and review dLazy service terms before use. <br>
Risk: The CLI can persist a dLazy API key in a local config file. <br>
Mitigation: Use npx or DLAZY_API_KEY for less persistent setup when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected. <br>
Risk: Generation consumes dLazy account credits and may fail when the account has insufficient balance. <br>
Mitigation: Use the dry-run option for cost estimates where possible and confirm available credits before long or repeated generations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Shell command guidance and JSON responses containing generated media URLs or async task metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and a pinned @dlazy/cli version 1.2.3; generated outputs are hosted on files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.4 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
