## Description: <br>
Shorten URLs via tinyurl or bitly API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other external users use this skill to generate shortened URLs from longer links, using Bitly when BITLY_TOKEN is configured and TinyURL otherwise. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shortened URLs can hide sensitive destinations or expose links that contain secrets. <br>
Mitigation: Do not shorten sensitive internal links, password-reset links, invite links, pre-signed URLs, or URLs containing secrets in query parameters. <br>
Risk: Using Bitly sends the destination URL through the configured Bitly account. <br>
Mitigation: Set BITLY_TOKEN only when the agent is intended to use that Bitly account; otherwise rely on the TinyURL fallback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/url-shorten) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text URL, with Markdown shell command examples when explaining usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl; Bitly usage depends on the optional BITLY_TOKEN environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
