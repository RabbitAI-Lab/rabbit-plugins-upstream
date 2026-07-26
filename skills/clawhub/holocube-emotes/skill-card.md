## Description: <br>
Control a GeekMagic holocube display as an AI emote system, generating holographic sprite kits with Gemini and switching expressions based on agent state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thrive-spencerj](https://clawhub.ai/user/thrive-spencerj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users with a GeekMagic HelloCubic-Lite or compatible holocube use this skill to give an AI assistant a physical emote display, including sprite generation, device setup, and state-based expression changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can probe the local network to discover holocube devices. <br>
Mitigation: Prefer passing a known device IP with --ip and run discovery only on networks where local scanning is acceptable. <br>
Risk: Sprite generation can use a stored Gemini API key. <br>
Mitigation: Use a dedicated Gemini API key for this workflow and review local configuration before running generation scripts. <br>
Risk: Device setup can clear or replace images on the selected holocube. <br>
Mitigation: Back up existing device images before setup and confirm the target device IP before using clear or upload options. <br>


## Reference(s): <br>
- [TOOLS.md Example - Holocube Section](references/tools-example.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts may generate image files and device configuration changes when run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local holocube device; sprite generation requires GEMINI_API_KEY and the nano-banana-pro skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
