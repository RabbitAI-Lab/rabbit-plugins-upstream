## Description: <br>
tax-ipo-tax helps agents provide IPO tax-compliance guidance, including tax incentive dependency review, disclosure planning, red-chip structure tax checks, self-check workflows, and risk remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to triage IPO-related tax compliance questions, run structured tax self-checks, identify disclosure and historical-tax risks, and produce practical remediation guidance. It is not a substitute for licensed tax, legal, audit, or filing services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive IPO, tax, or enterprise details may be sent to mcp.aitaxs.top for policy answers, risk checks, tax calculations, or web self-checks. <br>
Mitigation: Minimize or anonymize inputs, avoid confidential company identifiers, and use the skill only when cloud processing and the publisher's retention claims are acceptable. <br>
Risk: The skill stores API credentials, client identifiers, cached health state, and local logs of questions or scenarios on the user's device or in browser localStorage. <br>
Mitigation: Review and clear local skill data after use, run in a dedicated profile or sandbox for sensitive work, and avoid sharing local profiles that may contain credentials or logs. <br>
Risk: Optional MCP client setup can modify local agent configuration files when explicitly enabled. <br>
Mitigation: Review configuration changes before enabling automatic setup, keep backups, and disable automatic setup in managed or confidential environments unless approved. <br>
Risk: Tax-compliance guidance can be incomplete, outdated, or unsuitable for a specific IPO fact pattern. <br>
Mitigation: Treat outputs as triage and drafting support, verify against current official rules, and involve qualified tax, legal, audit, or filing professionals before taking action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [IPO tax compliance web workflow](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain-text guidance, with optional structured self-check results and configuration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP services for policy answers, risk checks, tax calculations, and knowledge-base metadata; offline workflows provide limited local reference guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
