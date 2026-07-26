## Description: <br>
Xia Desktop Agent helps agents automate Windows GUI tasks such as screenshots, clicks, typing, opening apps, WeChat messaging and file sends, and ToDesk remote-connection workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users who intentionally grant desktop-control access use this skill to run preset Windows workflows or natural-language desktop automation for local apps, WeChat, and ToDesk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad Windows desktop control, including application launching, screenshots, clicks, typing, messaging, file transfer, and remote-access workflows. <br>
Mitigation: Install only when this level of desktop authority is intended, constrain app launching and command execution, and require explicit confirmation before sensitive actions. <br>
Risk: Screenshots and ToDesk remote-access credentials can expose sensitive information. <br>
Mitigation: Treat screenshots, device codes, and temporary passwords as sensitive data; limit sharing, store them in protected locations, and delete them when no longer needed. <br>
Risk: Automated WeChat messages or file transfers could send content to the wrong recipient or disclose unintended files. <br>
Mitigation: Confirm the recipient, message text, and file path immediately before sending, and require a hard approval for each outbound message or file transfer. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or file outputs from Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create screenshot files and trigger desktop actions such as messages, file transfers, and application launches when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
