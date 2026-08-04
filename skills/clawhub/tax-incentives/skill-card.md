## Description: <br>
Tax Incentives helps users assess Chinese tax incentive eligibility, R&D super-deduction issues, high-tech enterprise qualification, western development incentives, specialized-enterprise benefits, and related compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and compliance practitioners use this skill to match Chinese tax incentives, check qualification requirements, estimate incentive treatment, and identify documentation or eligibility risks before relying on a benefit. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Confidential tax, financial, or company data may be sent to a remote cloud tax service. <br>
Mitigation: Install and use the skill only with clear consent to remote processing, and avoid sending sensitive identifiers unless they are necessary for the task. <br>
Risk: The skill may store an API key and logs under the user profile. <br>
Mitigation: Use it on trusted devices, restrict access to the local user profile, and clear local configuration, cache, or logs when credentials or sensitive work should no longer remain on the machine. <br>
Risk: MCP client configuration may be modified if autosetup is enabled or setup scripts are run. <br>
Mitigation: Review proposed MCP configuration changes before enabling autosetup, keep backups, and confirm the configured endpoint is expected. <br>
Risk: Tax incentive guidance can be time-sensitive and may not fit every fact pattern. <br>
Mitigation: Verify material conclusions against current official tax guidance or a qualified tax professional before filing, claiming, or relying on an incentive. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Tax incentives self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured text, MCP tool responses, local configuration snippets, and optional HTML self-check workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote cloud tax service and local fallback workflows; answers should be verified against official tax authorities or qualified professionals for material decisions.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
