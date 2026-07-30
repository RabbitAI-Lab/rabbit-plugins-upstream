## Description: <br>
Tax Incentives helps agents provide China-focused tax incentive and qualification guidance for high-tech enterprise status, R&D super-deduction, Western Development incentives, specialized-and-new enterprise support, VAT add-on deductions, incentive matching, self-checks, and compliance risk warnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance practitioners use this skill to ask incentive eligibility questions, compare China tax incentive programs, run lightweight qualification self-checks, and get risk-aware next steps before formal filing or professional review. <br>

### Deployment Geography for Use: <br>
Global (content focuses on China tax incentives and compliance) <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and risk scenarios may be sent to the third-party service at mcp.aitaxs.top. <br>
Mitigation: Avoid entering confidential company identifiers, regulated personal data, or unreleasable financial details unless the service terms and retention practices are acceptable. <br>
Risk: Credentials and logs may be stored locally. <br>
Mitigation: Review the local client configuration and log locations before use, restrict file access, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Optional setup code can modify MCP client configuration when explicitly run or enabled. <br>
Mitigation: Keep setup in dry-run mode until configuration changes have been reviewed, and enable automatic setup only in trusted environments. <br>
Risk: Tax incentive guidance can become outdated or may not fit a specific taxpayer's facts. <br>
Mitigation: Validate material filing, qualification, or payment decisions against official sources and qualified tax professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax incentives self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown and plain text responses with optional command snippets, configuration guidance, and structured tool results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax questions, risk checks, calculations, and knowledge-base lookups through a third-party MCP service; offline workflows provide limited local reference guidance.] <br>

## Skill Version(s): <br>
3.15.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
