## Description: <br>
Searches the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices before TTS selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search dLazy's hosted ElevenLabs voice search service and choose candidate voices with previewable results before text-to-speech work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and filters are sent to the hosted dLazy API. <br>
Mitigation: Use the skill for voice search terms and filters, and avoid sending sensitive text as search prompts. <br>
Risk: The skill uses a saved or environment-provided dLazy API key. <br>
Mitigation: Install and run it only where storing or passing a dLazy API key is acceptable, and rotate or revoke the key from the dLazy dashboard when needed. <br>
Risk: The artifact contains stale generic output and media-upload documentation that may not reflect this command's actual behavior. <br>
Mitigation: Treat those sections as generic CLI boilerplate and rely on the elevenlabs-search command help and returned JSON for command-specific behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [JSON CLI result with command and authentication guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.] <br>

## Skill Version(s): <br>
1.3.4 (source: server evidence release.version and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
