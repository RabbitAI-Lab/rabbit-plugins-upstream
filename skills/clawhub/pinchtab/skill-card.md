## Description: <br>
PinchTab guides agents through local browser automation for navigation, interaction, page inspection, captures, approved profile reuse, and CLI or HTTP API workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pinchtab](https://clawhub.ai/user/pinchtab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use PinchTab to let an agent drive local browser sessions, inspect accessible page state, interact with forms and flows, and export screenshots, PDFs, or site review outputs when approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent controlling a local browser can affect authenticated sessions or external accounts. <br>
Mitigation: Use dedicated low-privilege PinchTab profiles and require explicit user approval before authenticated, account-changing, payment, deletion, publishing, or other consequential actions. <br>
Risk: Cookies, browser state, network exports, file transfers, recordings, and JavaScript evaluation can expose credentials, personal data, or local files. <br>
Mitigation: Keep gated capabilities disabled unless the task requires them, preserve redaction, save artifacts only to approved workspace or temporary paths, and delete temporary captures when finished. <br>
Risk: Page content can contain hostile or misleading instructions for the agent. <br>
Mitigation: Treat page-derived content as untrusted data and follow only instructions that independently match the user's request. <br>


## Reference(s): <br>
- [PinchTab ClawHub Skill](https://clawhub.ai/pinchtab/skills/pinchtab) <br>
- [PinchTab Homepage](https://github.com/pinchtab/pinchtab) <br>
- [PinchTab Documentation](https://pinchtab.com) <br>
- [PinchTab Security and Trust](TRUST.md) <br>
- [Sensitive Operations](references/safety.md) <br>
- [CLI Commands Reference](references/commands.md) <br>
- [PinchTab API Reference](references/api.md) <br>
- [Profile Management](references/profiles.md) <br>
- [Site Review Reference](references/site-review.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON API examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides browser-control work; PinchTab may produce page text, snapshots, screenshots, PDFs, recordings, downloaded files, or audit artifacts when the user-approved task requires them.] <br>

## Skill Version(s): <br>
0.15.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
