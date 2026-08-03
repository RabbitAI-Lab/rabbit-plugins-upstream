## Description: <br>
Formats Telegram replies using Telegram's actual supported formatting - when to use bold, code, quotes, headings, and structure without overusing them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pedram-naghib](https://clawhub.ai/user/pedram-naghib) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to write Telegram replies with formatting that matches Telegram HTML and OpenClaw rich-message behavior. It helps choose when to use plain text, inline tags, headings, tables, blockquotes, and fallback structure without over-formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rich Telegram formatting can render incorrectly when OpenClaw rich-message behavior, Telegram client support, or image captions do not match the tested conditions. <br>
Mitigation: Check the rich-message setting and OpenClaw version before relying on rich blocks, send a small test message when behavior is uncertain, and use standard HTML formatting for image captions or unsupported clients. <br>


## Reference(s): <br>
- [Telegram Bot Features: Rich Messages](https://core.telegram.org/bots/features#rich-messages) <br>
- [OpenClaw issue 14027: outbound Telegram media groups](https://github.com/openclaw/openclaw/issues/14027) <br>
- [ClawHub skill page](https://clawhub.ai/pedram-naghib/skills/telegram-formatting) <br>
- [Publisher profile](https://clawhub.ai/user/pedram-naghib) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline Telegram HTML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is conditional on Telegram rich-message configuration, OpenClaw version, attached images, and client support.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
