## Description: <br>
Installs and maintains a local-only Übersicht desktop widget that displays Codex token usage, recent root sessions, source labels, and context-window pressure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinadu-ai](https://clawhub.ai/user/tinadu-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers who use Codex on macOS use this skill to install, update, inspect, or uninstall a local Übersicht widget for monitoring token usage and recent session activity without sending data to external services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The widget repeatedly reads local Codex usage files and displays session metadata on the desktop. <br>
Mitigation: Install it only on machines where local Codex usage visibility is acceptable, and remove it with the provided uninstall script when the display is no longer desired. <br>
Risk: The installer creates or replaces the widget directory under the user's Übersicht widgets folder. <br>
Mitigation: Review the install destination before running the script; the documented behavior is limited to the codex-usage.widget directory. <br>
Risk: Codex local storage fields may change between Codex releases, which can make the widget's metrics incomplete or inaccurate. <br>
Mitigation: Validate the installed Python reader returns JSON with ok set to true after installation or Codex updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tinadu-ai/skills/codex-usage-widget) <br>
- [Übersicht](https://tracesof.net/uebersicht/) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and local widget files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local installation, validation, update, and uninstall guidance for an Übersicht widget; does not produce network API calls.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
