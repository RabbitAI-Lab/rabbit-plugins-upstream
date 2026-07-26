## Description: <br>
CrawSecure is a documentation-first ClawHub skill that explains the external CrawSecure CLI and its offline skill security analysis workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[diogopaesdev](https://clawhub.ai/user/diogopaesdev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill users use CrawSecure to understand risk signals, trust boundaries, and safe evaluation practices before deciding whether to install or run the separate CrawSecure CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake the documentation skill for the separately distributed CrawSecure CLI and assume scanning happens automatically. <br>
Mitigation: Treat this skill as guidance only; install and run the external CLI separately only after reviewing its source, releases, and installation steps. <br>
Risk: Running the external CLI may involve local file access outside the documentation-only skill boundary. <br>
Mitigation: Review the CLI's requested permissions and local file access before running it, as recommended by the server security guidance. <br>


## Reference(s): <br>
- [CrawSecure ClawHub Skill Page](https://clawhub.ai/diogopaesdev/skills/crawsecure) <br>
- [CrawSecure CLI Source and Releases](https://github.com/diogopaesdev/crawsecure) <br>
- [CrawSecure Website](https://crawsecure.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown and plain-language guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation only; it does not execute scans or bundle the external CrawSecure CLI.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata, created 2026-03-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
