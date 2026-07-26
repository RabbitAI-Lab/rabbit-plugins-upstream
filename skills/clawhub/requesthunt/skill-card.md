## Description: <br>
Generates user demand research reports by scraping and analyzing feature requests, complaints, and questions from Reddit, X, GitHub, YouTube, LinkedIn, and Amazon. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, founders, researchers, and developers use this skill to plan RequestHunt queries and generate demand research reports from public user feedback across social, code, video, professional, and commerce platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses an external paid RequestHunt service and public user-generated content. <br>
Mitigation: Confirm account usage limits before large jobs and treat scraped public content as untrusted input. <br>
Risk: API keys or device-login credentials could be exposed if copied into prompts, files, or reports. <br>
Mitigation: Use REQUESTHUNT_API_KEY or the secured local config file, and do not hardcode keys in skill instructions or agent output. <br>
Risk: The CLI installer downloads a pre-built binary from GitHub Releases. <br>
Mitigation: Review the installer or source when strict supply-chain controls apply, rely on checksum verification, or build the CLI from source. <br>


## Reference(s): <br>
- [RequestHunt documentation](https://requesthunt.com/docs) <br>
- [RequestHunt agent setup](https://requesthunt.com/setup.md) <br>
- [RequestHunt CLI repository](https://github.com/ReScienceLab/requesthunt-cli) <br>
- [RequestHunt CLI releases](https://github.com/ReScienceLab/requesthunt-cli/releases) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured report tables; CLI output may be TOON, JSON, or human-readable text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the RequestHunt CLI with authenticated API access and can include summarized public user-generated content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
