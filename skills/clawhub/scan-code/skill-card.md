## Description: <br>
CodeGuard MCP是一款实时AI代码安全扫描工具，用于检测AI生成代码中的漏洞、密钥和合规性问题，适用于开发环境中的代码安全审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scan code for vulnerabilities, exposed secrets, secure-fix suggestions, and compliance concerns during development review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scanned code, embedded secrets, vulnerability details, and compliance context may be sent to the XiaoBenYang remote API. <br>
Mitigation: Use only with code that policy allows sharing with that provider; avoid proprietary or regulated code unless approved. <br>
Risk: The skill stores the XiaoBenYang API key in a local plaintext .env file. <br>
Mitigation: Use a limited-scope API key and remove or protect the .env file after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/scan-code) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include vulnerability findings, secret-detection results, compliance checks, and secure-fix suggestions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
