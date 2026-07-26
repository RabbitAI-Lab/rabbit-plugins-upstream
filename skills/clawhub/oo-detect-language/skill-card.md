## Description: <br>
Detect Language (detectlanguage.com). Use this skill for Detect Language requests involving language detection, supported-language lookup, and account-status retrieval through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to route Detect Language tasks through an OOMOL-connected account, including detecting text language, checking supported languages, and reviewing account status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for language detection may contain sensitive content and is routed through OOMOL as an intermediary to Detect Language. <br>
Mitigation: Avoid sending sensitive text unless the user's privacy requirements permit that routing. <br>
Risk: First-time setup may require installing the oo CLI from a remote installer. <br>
Mitigation: Review the installer before running it when the CLI is missing. <br>


## Reference(s): <br>
- [Detect Language homepage](https://detectlanguage.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-detect-language) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output from the connector] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can return language detection results, supported-language lists, account status, or setup guidance depending on the requested action.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
