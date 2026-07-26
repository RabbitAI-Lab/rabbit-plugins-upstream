## Description: <br>
Climb the browser ladder - start free, escalate only when needed across static fetches, local Playwright, BrowserCat, and Browserless.io for higher-friction browsing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ktpriyatham](https://clawhub.ai/user/ktpriyatham) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to choose a browser automation rung for URL access, starting with static fetches and escalating to local or cloud browser services only when needed. It supports page checks, HTML retrieval, screenshots, PDFs, and setup guidance for optional cloud browser credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud browser escalation can send browsing targets to third-party browser services. <br>
Mitigation: Use local rungs when possible and do not use cloud rungs for private, internal, authenticated, regulated, or credential-bearing pages without explicit approval. <br>
Risk: CAPTCHA, Cloudflare, and similar protections may represent an authorization checkpoint. <br>
Mitigation: Treat protected flows as requiring explicit authorization instead of automatically escalating to bypass-capable services. <br>
Risk: The security verdict is suspicious due to high-risk browser escalation behavior. <br>
Mitigation: Review the skill before deployment and restrict use to cases where advanced web automation and optional third-party browser services are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ktpriyatham/skills/browser-ladder) <br>
- [BrowserCat](https://browsercat.com) <br>
- [Browserless.io](https://browserless.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands, JavaScript snippets, and environment variable configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce fetched HTML, screenshots, or PDFs when the bundled browse script is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
