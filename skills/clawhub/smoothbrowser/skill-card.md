## Description: <br>
SmoothBrowser helps agents use the Smooth CLI to run browser sessions for web navigation, form filling, scraping, app testing, file handling, and authenticated workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antoniocirclemind](https://clawhub.ai/user/antoniocirclemind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use SmoothBrowser when an agent needs to navigate websites, extract structured web data, test web apps, upload or download files, reuse browser profiles, or complete browser tasks that may require authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad third-party browser control over websites, logins, files, JavaScript execution, and saved sessions. <br>
Mitigation: Use anonymous or read-only sessions when possible, restrict allowed URLs, avoid sensitive files unless necessary, and require explicit approval before high-impact actions. <br>
Risk: Reusing logged-in profiles can expose account state or allow unintended form submissions, purchases, posts, downloads, or account setting changes. <br>
Mitigation: Keep profiles purpose-specific, use read-only profile mode for review tasks, and ask the user before reusing authenticated profiles or submitting changes. <br>
Risk: Browser automation can interact with untrusted web content and may encounter deceptive prompts or unsafe pages. <br>
Mitigation: Constrain sessions to expected sites, review task goals before execution, and close sessions when work is complete. <br>


## Reference(s): <br>
- [ClawHub SmoothBrowser listing](https://clawhub.ai/antoniocirclemind/skills/smoothbrowser) <br>
- [Smooth account and API key portal](https://app.smooth.sh) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Smooth commands can return plain text or JSON output depending on command options; browser sessions may use profiles, allowed URL patterns, uploaded file IDs, response schemas, and task metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
