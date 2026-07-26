## Description: <br>
Forges reusable agent skill packages from browser-act website exploration so agents can repeat verified extraction or browser-operation workflows without re-exploring the site. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation builders use this skill to turn a website exploration session into reusable agent-callable skill packages for data extraction or browser operations. It is most useful when repeated or large-volume browser tasks need a verified approach before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill generates powerful browser automation packages and may under-describe write actions or state-changing behavior. <br>
Mitigation: Review generated SKILL.md files and scripts before installation, supervise state-changing actions, and test workflows in a non-sensitive browser session first. <br>
Risk: The security evidence flags rate-limit evasion guidance and cautions against using stealth session or fingerprint guidance to bypass site controls. <br>
Mitigation: Use the skill only on sites and accounts where automation is authorized, respect site controls and rate limits, and avoid stealth or fingerprint guidance for bypass. <br>
Risk: Generated workflows can inspect logged-in browser pages, network traffic, HAR recordings, and local extraction results. <br>
Mitigation: Use only accounts and data the user is authorized to access, keep outputs local unless intentionally shared, and remove sensitive records from generated artifacts before distribution. <br>


## Reference(s): <br>
- [BrowserAct homepage](https://www.browseract.com) <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/browser-act-skill-forge-skill) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown instructions with generated SKILL.md files, Python scripts, and shell command templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated packages are intended to be reviewed, tested, and installed before reuse.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact metadata reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
