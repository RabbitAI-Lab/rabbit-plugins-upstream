## Description: <br>
Create polished audio episodes with TTS narration, cover images, Spotify timelines, and show or episode management, then save them to the user's Spotify library. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spotify](https://clawhub.ai/user/spotify) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn authorized source material or user-provided audio into private Spotify episodes with narration, show notes, cover art, and timeline companions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installer and setup steps can modify the local environment and connect the user's Spotify account. <br>
Mitigation: Ask for explicit approval before installation or setup, and review the installer before running it. <br>
Risk: Spotify bearer tokens or other credentials could be exposed in logs, prompts, or copied output. <br>
Mitigation: Keep tokens out of prompts and logs, redact command output when needed, and avoid sharing token-bearing JSON. <br>
Risk: Uploaded episodes, timelines, and generated metadata use connected personal account data. <br>
Mitigation: Confirm the target show, upload action, and privacy expectation before saving, and state that saved episodes are private to the user. <br>
Risk: Cloud TTS or image providers may process episode text, prompts, or source content outside the user's local machine. <br>
Mitigation: Confirm the selected provider and avoid sensitive, confidential, or regulated content unless the user accepts the provider's processing terms. <br>
Risk: Generated episodes can infringe third-party rights if the source material is not authorized for this use. <br>
Mitigation: Use authorized APIs and user-provided or otherwise permitted content, preserve source links, and avoid representing third-party material as sponsored or original when it is not. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spotify/skills/save-to-spotify) <br>
- [CLI Usage](references/cli-usage.md) <br>
- [Spotify API](references/spotify-api.md) <br>
- [Audio Providers & Assembly](references/audio-providers.md) <br>
- [Timeline](references/timeline.md) <br>
- [Episode Description Format](references/episode-description.md) <br>
- [Cover Image](references/cover-image.md) <br>
- [Content Quality](references/content-quality.md) <br>
- [First-Time Onboarding](references/onboarding.md) <br>
- [Local Preview](references/local-preview.md) <br>
- [Recipes](references/recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, code snippets, and generated episode asset files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide the agent to produce MP3 audio, timeline JSON, HTML episode descriptions, cover images, and Spotify upload commands.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
