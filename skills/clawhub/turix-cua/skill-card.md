## Description: <br>
Computer Use Agent (CUA) for macOS automation using TuriX for visual desktop tasks such as opening apps, clicking buttons, and navigating UIs that do not have a CLI or API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tongyu-yan](https://clawhub.ai/user/tongyu-yan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs supervised macOS GUI automation for workflows that are difficult or unavailable through command-line tools or APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an AI agent broad control over a Mac desktop. <br>
Mitigation: Install it only when desktop control is intended, supervise runs, and use a reviewed or pinned TuriX-CUA checkout. <br>
Risk: Desktop automation can affect sensitive accounts, files, submissions, uploads, purchases, or deletions. <br>
Mitigation: Avoid personal or production accounts and require explicit confirmation before uploads, submissions, sending files, account changes, purchases, or deletions. <br>
Risk: Screen Recording and Accessibility permissions can expose desktop content or enable unintended actions after use. <br>
Mitigation: Grant only the required macOS permissions for the run and revoke Screen Recording and Accessibility permissions when finished. <br>


## Reference(s): <br>
- [TuriX Computer Use on ClawHub](https://clawhub.ai/tongyu-yan/skills/turix-cua) <br>
- [tongyu-yan ClawHub profile](https://clawhub.ai/user/tongyu-yan) <br>
- [TuriX-CUA repository](https://github.com/TurixAI/TuriX-CUA) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS Screen Recording and Accessibility permissions for desktop control.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
