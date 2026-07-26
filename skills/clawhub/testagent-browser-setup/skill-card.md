## Description: <br>
One-time installation and initialization of Chromium, system dependencies, Chinese fonts, and the CDP launcher script in a fresh openclaw environment with no root required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangyin717](https://clawhub.ai/user/wangyin717) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and test engineers use this skill to prepare a fresh OpenClaw environment for browser-based testing, screenshots, direct CDP control, and optional browser-use workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad browser control, session handling, network access, package installation, and OpenClaw MCP configuration changes. <br>
Mitigation: Review before installing and use only in an isolated test environment where these capabilities are explicitly approved. <br>
Risk: Direct CDP control and optional browser-use workflows can interact with authenticated browser state or sensitive sessions. <br>
Mitigation: Avoid reusing real Chrome profiles or authenticated sessions unless the target, account, and session scope are authorized. <br>
Risk: Cloud browser, tunnel, residential proxy, and anti-bot capabilities can affect external services beyond routine local testing. <br>
Mitigation: Use these capabilities only with documented authorization and a defined target scope. <br>
Risk: SSRF policy blocks may indicate a security boundary. <br>
Mitigation: Treat policy blocks as security decisions and do not work around them without explicit approval. <br>
Risk: The setup path performs remote downloads and package installs. <br>
Mitigation: Run setup only where remote installs are permitted, and review downloaded scripts, packages, and assets before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangyin717/skills/testagent-browser-setup) <br>
- [Browser tools guide](artifact/TOOLS.md) <br>
- [browser-use repository](https://github.com/browser-use/browser-use) <br>
- [WenQuanYi Micro Hei font asset](https://github.com/anthonyfok/fonts-wqy-microhei/raw/master/wqy-microhei.ttc) <br>
- [browser-use CLI installer](https://browser-use.com/cli/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown with bash, JSON, and JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup commands, OpenClaw browser configuration guidance, direct CDP examples, and smoke-test steps.] <br>

## Skill Version(s): <br>
1.0.10 (source: server-resolved ClawHub release evidence; artifact frontmatter says 2.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
