## Description: <br>
一个基于Model Context Protocol (MCP)的代码审查工具服务器，提供多维度的代码审查和打分功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to submit code, Git diffs, or individual file contents to a remote Xiaobenyang review service and receive review output or parsed scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed code, diffs, file paths, and review text are sent to a remote Xiaobenyang API. <br>
Mitigation: Use the skill only on repositories approved for that provider, and review the provider's retention and confidentiality terms before submitting sensitive code. <br>
Risk: The XBY_APIKEY credential is stored in a local .env file and also copied into the process environment. <br>
Mitigation: Keep .env out of version control, restrict local file access, and rotate the key if it may have been exposed. <br>
Risk: The artifact contains gaokao-related configuration and documentation leftovers that do not match a code-review release. <br>
Mitigation: Resolve the naming and configuration mismatch before production use so operators can verify the correct API identifiers and behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/xby-review-code) <br>
- [Xiaobenyang service](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON responses from remote tool calls, typically summarized for the user as Markdown review text or scores] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value; sends code, diffs, file paths, and review text to a remote API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
