## Description: <br>
Lightpanda browser is a drop-in replacement for Chrome and the OpenClaw default browser for faster, lighter data retrieval and browser automation tasks that do not need graphical rendering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krichprollsch](https://clawhub.ai/user/krichprollsch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to install and run the Lightpanda headless browser as a low-resource CDP endpoint for data extraction, web automation, and controlled search workflows. It is intended for Linux and macOS environments where Playwright, Puppeteer, or direct CDP clients can connect to a local browser server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer downloads a Lightpanda nightly binary from GitHub, so release-channel trust and binary freshness affect the runtime. <br>
Mitigation: Install only when the Lightpanda GitHub nightly release channel is trusted, and rely on the script's checksum verification before running the binary. <br>
Risk: CDP clients can control and inspect the browser session. <br>
Mitigation: Bind the browser server to 127.0.0.1, close it when finished, and avoid sensitive logged-in sessions with untrusted automation scripts. <br>
Risk: Lightpanda is under active development and may have crashes or site-compatibility issues. <br>
Mitigation: Update with scripts/install.sh when issues occur and report reproducible failures with the script, target URL, and expected versus actual results. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/krichprollsch/skills/lightpanda-browser) <br>
- [Lightpanda agent skill source](https://github.com/lightpanda-io/agent-skill) <br>
- [Lightpanda browser issues](https://github.com/lightpanda-io/browser/issues) <br>
- [Lightpanda nightly release API](https://api.github.com/repos/lightpanda-io/browser/releases/tags/nightly) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes installation commands, CDP server configuration, and Playwright or Puppeteer connection examples.] <br>

## Skill Version(s): <br>
1.0.3 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
