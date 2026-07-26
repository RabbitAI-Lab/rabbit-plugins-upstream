## Description: <br>
Provides OpenClaw guidance and code examples for using the WrynAI SDK to crawl sites, extract page content, parse search results, and capture screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wrynai](https://clawhub.ai/user/wrynai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to gather public web content, documentation, search results, links, structured text, and screenshots through WrynAI-powered crawling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target URLs, search queries, extracted page contents, and screenshots may be sent to WrynAI. <br>
Mitigation: Use this skill only for pages approved for third-party processing, and avoid private, internal, regulated, or secret-bearing pages unless explicitly authorized. <br>
Risk: Screenshot capture can write a local screenshot.png file. <br>
Mitigation: Remove, rename, or handle screenshot files according to the workflow's data retention and sharing requirements. <br>
Risk: The skill depends on the third-party wrynai package and a WrynAI API key. <br>
Mitigation: Verify the package source before installation and use a revocable API key with appropriate access controls. <br>


## Reference(s): <br>
- [WrynAI Documentation](https://docs.wryn.ai) <br>
- [WrynAI API Signup](https://wryn.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/wrynai/skills/wrynai-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell code snippets; helper outputs include dictionaries, lists, text, markdown, links, structured data, and screenshot files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the wrynai Python package and a WRYNAI_API_KEY environment variable; examples include crawl limits, timeout settings, and retry handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact version information) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
