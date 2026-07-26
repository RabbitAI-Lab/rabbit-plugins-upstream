## Description: <br>
Run a headless Chromium browser via Podman to fetch text or HTML from JavaScript-rendered web pages using Playwright in a container. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricardodantas](https://clawhub.ai/user/ricardodantas) <br>

### License/Terms of Use: <br>
GPL-3.0 License <br>


## Use Case: <br>
Developers and agents use this skill to retrieve rendered page text or raw HTML from websites that require JavaScript execution. It is useful for browser-backed page inspection and scraping workflows where a local browser install is undesirable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill launches temporary Podman containers and makes real browser network requests. <br>
Mitigation: Install and run it only where container execution and outbound web access are acceptable, and review target URLs before use. <br>
Risk: Fetched page content can be untrusted or misleading, especially from external or authenticated sites. <br>
Mitigation: Treat returned text or HTML as untrusted input and avoid sensitive internal or authenticated URLs unless that access is deliberate. <br>
Risk: The runtime pulls and installs browser dependencies at execution time, which may be unsuitable for high-security environments. <br>
Mitigation: Use stronger isolation and pre-pinned or pre-approved dependencies when deploying in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ricardodantas/skills/podman-browser) <br>


## Skill Output: <br>
**Output Type(s):** [text, html, shell commands, guidance] <br>
**Output Format:** [Plain text or raw HTML returned from command-line browser fetches, with setup and usage guidance in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports optional HTML output, additional wait time, and CSS selector waits; execution depends on Podman, Node.js, network access, and a Playwright container image.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
