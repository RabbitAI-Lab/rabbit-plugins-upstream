## Description: <br>
Automates iOS Simulator workflows with simctl and optional idb for device lifecycle, app management, push notifications, privacy grants, screenshots, and accessibility-based UI navigation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agents working on iOS apps use this skill to manage simulators, install and launch apps, capture screenshots or video, adjust simulator state, and inspect or interact with UI through accessibility data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing simulator commands can affect the wrong simulator or app when the UDID or bundle ID is incorrect. <br>
Mitigation: Confirm the selected UDID and bundle ID before running install, launch, privacy, push, clipboard, openurl, erase, or delete commands. <br>
Risk: Erase and delete operations can remove simulator data or devices. <br>
Mitigation: Require explicit user confirmation and use the skill's documented --yes requirement only after reviewing the target. <br>
Risk: The skill depends on local macOS tooling and optional idb packages that may vary by environment. <br>
Mitigation: Install only on trusted macOS development hosts or nodes, run the health check first, and pin or audit Homebrew and pip dependencies when required by policy. <br>


## Reference(s): <br>
- [Troubleshooting](references/TROUBLESHOOTING.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/tristanmanchester/skills/ios-simulator) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands; CLI output is single-line JSON by default, with optional text summaries and generated PNG or MP4 files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS with Xcode tools for simulator control; idb is optional but required for accessibility-tree inspection and semantic UI input.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
