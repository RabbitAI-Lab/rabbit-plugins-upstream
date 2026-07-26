## Description: <br>
Add browser audio notifications to Moltbot/Clawdbot webchat with five intensity levels, custom sounds, and tab-aware playback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brokemac79](https://clawhub.ai/user/brokemac79) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and webchat maintainers use this skill to add configurable browser sound alerts for new chat messages, mentions, and direct messages while keeping playback limited to background tabs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser audio may be blocked until the user interacts with the page. <br>
Mitigation: Expose the provided enable or test control so users can unlock audio before relying on background notifications. <br>
Risk: Preferences and uploaded custom sounds are stored in browser localStorage. <br>
Mitigation: Review localStorage behavior for the deployment, keep uploaded sounds small and non-sensitive, and document that data remains in the user's browser. <br>
Risk: The settings panel and scripts run in the host webchat page. <br>
Mitigation: Serve the bundled scripts, settings panel, and sounds from the same trusted origin as the webchat and review local modifications before deployment. <br>
Risk: Publishing examples include command-line token usage. <br>
Mitigation: Prefer the browser login flow for ClawHub publishing or maintenance and avoid pasting tokens into shared shells or documentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brokemac79/skills/webchat-audio-notifications) <br>
- [Integration guide](docs/integration.md) <br>
- [Easy setup guide](docs/EASY_SETUP.md) <br>
- [Howler.js](https://howlerjs.com/) <br>
- [Mixkit sound attribution](client/sounds/SOUNDS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, JavaScript, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces browser integration steps and configuration examples for installing notification scripts, settings UI, sounds, and event hooks.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
