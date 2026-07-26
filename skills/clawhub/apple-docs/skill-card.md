## Description: <br>
Query Apple Developer Documentation, APIs, and WWDC videos (2014-2025). Search SwiftUI, UIKit, Objective-C, Swift frameworks and watch sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and Apple platform engineers use this skill to search Apple Developer documentation, inspect API and platform compatibility details, browse sample code and technology guides, and retrieve WWDC session information from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The doc command accepts full URLs and can retrieve content outside Apple Developer documentation if the URL is reachable. <br>
Mitigation: Prefer Apple documentation paths such as /documentation/... and review or restrict any full URL before allowing the agent to fetch it. <br>
Risk: The skill makes outbound network requests for documentation search, Apple documentation data, and GitHub-hosted WWDC data. <br>
Mitigation: Install it only in environments where outbound documentation lookups are acceptable, and apply network allowlists when stricter controls are required. <br>
Risk: Documentation and WWDC search results may be incomplete, stale, or parsed from public web responses rather than authoritative local SDK metadata. <br>
Mitigation: Use results as developer guidance and verify important API availability, deprecations, and behavior against Apple documentation or SDK tooling before release decisions. <br>


## Reference(s): <br>
- [Apple Docs on ClawHub](https://clawhub.ai/thesethrose/skills/apple-docs) <br>
- [Apple Docs MCP Server](https://github.com/kimsungwhee/apple-docs-mcp) <br>
- [Apple Developer Documentation](https://developer.apple.com/documentation/) <br>
- [Apple Developer](https://developer.apple.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Console text, Markdown-like documentation summaries, JSON result payloads, and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and makes outbound requests to Apple Developer documentation endpoints and GitHub-hosted WWDC data. Some commands support result limits, framework, category, year, and transcript options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
