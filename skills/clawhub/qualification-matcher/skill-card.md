## Description: <br>
Qualification Matcher compares bid qualification requirements against a company qualification database, generates detailed scores and rankings, and flags uncertain matches for manual review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincheng0307](https://clawhub.ai/user/xincheng0307) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams and business development staff use this skill to evaluate whether companies meet tender qualification requirements, compare scoring outcomes, and prepare qualification review reports from Word, PDF, or Excel bid documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tender documents and company qualification data may be sent to Alibaba Cloud DashScope during matching and extraction. <br>
Mitigation: Use only documents approved for third-party processing, redact sensitive pricing or proprietary content where possible, and disclose the cloud processing dependency before use. <br>
Risk: The workflow requires a DashScope API key and stores configuration in a local config file. <br>
Mitigation: Protect the API key, avoid committing generated configuration files, and rotate credentials if they are exposed. <br>
Risk: The reviewed artifact refers to a Windows EXE that was not present for review. <br>
Mitigation: Verify the executable from a trusted source and scan it before running it on confidential bid materials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xincheng0307/skills/qualification-matcher) <br>
- [Publisher profile](https://clawhub.ai/user/xincheng0307) <br>
- [Alibaba Cloud DashScope console](https://dashscope.console.aliyun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Analysis, Files] <br>
**Output Format:** [Markdown guidance with generated Excel result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied bid documents, a qualification workbook, and an Alibaba Cloud DashScope API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
