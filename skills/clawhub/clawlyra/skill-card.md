## Description: <br>
Give your OpenClaw agent a face and a voice: reply as Lyra, a warm 3D avatar companion, and emit her inline performance tags so the self-hosted Lyra app speaks and performs your replies live: expressions, gestures, scene changes, lip-synced voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freespirits](https://clawhub.ai/user/freespirits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Clawlyra to make an OpenClaw agent respond as Lyra, emitting inline affect, gesture, scene, name, and audio-emotion tags that a separately running Lyra app can speak and perform through a 3D avatar. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Lyra sidecar needs an OpenClaw gateway token, which could expose agent access if mishandled. <br>
Mitigation: Keep OPENCLAW_TOKEN in a private local environment file, exclude it from source control, and rotate it if exposed. <br>
Risk: Agent replies may be spoken aloud by the Lyra app and disclose sensitive information to nearby people. <br>
Mitigation: Use the skill only in settings where spoken output is appropriate for the information being discussed. <br>
Risk: Installing only the skill will not render voice or a 3D avatar because the Lyra app is a required sidecar. <br>
Mitigation: Run the self-hosted Lyra app with LLM_PROVIDER=openclaw and a valid OpenClaw gateway token before expecting spoken or animated output. <br>


## Reference(s): <br>
- [Lyra app homepage](https://github.com/Freespirits/lyra-ai-companion) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [Clawlyra on ClawHub](https://clawhub.ai/freespirits/skills/clawlyra) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Plain spoken prose with inline bracketed performance tags] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Every reply should begin with an affect tag and may include gesture, scene, name, and audio-emotion tags for the Lyra sidecar.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
