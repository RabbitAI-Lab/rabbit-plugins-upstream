## Description: <br>
Helps users assess Chinese tax-incentive eligibility, run qualification self-checks, and produce compliance guidance for high-tech enterprise, R&D deduction, western development, specialized-new, and related incentive scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, and compliance teams use this skill to triage Chinese tax-incentive eligibility, identify qualification and documentation risks, and generate self-check guidance before professional or authority review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and calculation inputs may be sent to the publisher's remote service. <br>
Mitigation: Use anonymized or aggregated facts where possible, and do not enter taxpayer identifiers, private account details, or confidential transaction data without approval. <br>
Risk: Raw prompts and scenarios may be written to local logs. <br>
Mitigation: Avoid submitting secrets or personal data, and periodically review or purge the local tax-policy client logs when handling sensitive matters. <br>
Risk: The matrix installer can add related skills and may download additional packages when configured. <br>
Mitigation: Require explicit user confirmation before installation and inspect the matrix or run a dry-run path before adding related skills. <br>
Risk: Tax-incentive conclusions are time-sensitive and depend on facts, region, and authority interpretation. <br>
Mitigation: Confirm material filings, qualification claims, and risk responses with the applicable tax authority or a qualified tax professional. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax incentives web self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured self-check summaries, shell command and configuration snippets, and copied prompts for deeper analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP tax-policy service with local/offline fallback workflows; users should treat generated tax guidance as preliminary.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
