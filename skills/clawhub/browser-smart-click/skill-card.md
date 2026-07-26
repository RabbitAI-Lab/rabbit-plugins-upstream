## Description: <br>
Retry browser clicks with automatic obstacle detection and dismissal when cookie banners, modals, fixed headers, or other overlays block the target element. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and browser automation agents use this skill to recover from Playwright or OpenClaw browser click failures caused by obstructing page elements. It helps detect blockers, optionally dismiss common popups, retry clicks, and report structured click status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic dismissal may accept cookie, consent, or similar banners during browser automation. <br>
Mitigation: Use auto_dismiss=False or review calls manually when privacy consent, account dialogs, purchases, or other meaningful site actions could be affected. <br>
Risk: JavaScript click fallback or forced clicking may bypass normal interactability checks. <br>
Mitigation: Use force and retry fallbacks only on targets that have been inspected and are safe to activate. <br>


## Reference(s): <br>
- [Browser Smart Click usage guide](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/browser-smart-click) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples and JSON ClickResult objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runtime helpers can return success, target, blocked, blocker, retry_count, and message fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
