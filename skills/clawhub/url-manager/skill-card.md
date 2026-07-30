## Description: <br>
Cross-platform URL collection and knowledge management with agent-first auto-registration for saving, organizing, searching, and sharing web resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[piccolo123](https://clawhub.ai/user/piccolo123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to save links or notes, organize them into categories and shared collections, search stored resources, and return a magic link for viewing the card-based library. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal use can create a hosted account, upload saved URLs or notes, and store credentials locally. <br>
Mitigation: Before first use, confirm account creation and data upload with the user, disclose that data is stored on ai.ocean94.com, and treat the local .token file and magic links as credentials. <br>
Risk: The documented fallback install path relies on an unpinned GitHub script when the bundled script is missing. <br>
Mitigation: Use the bundled artifact script when available, and avoid the fallback install path unless the source and revision have been independently verified. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/piccolo123/skills/url-manager) <br>
- [Publisher profile](https://clawhub.ai/user/piccolo123) <br>
- [Hosted URL Manager service](https://ai.ocean94.com) <br>
- [User Agreement](https://ai.ocean94.com/terms.html) <br>
- [Privacy Policy](https://ai.ocean94.com/privacy.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or text responses with optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and network access to ai.ocean94.com; command use can create a hosted account, save content remotely, and persist a local token.] <br>

## Skill Version(s): <br>
2.6.4 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
