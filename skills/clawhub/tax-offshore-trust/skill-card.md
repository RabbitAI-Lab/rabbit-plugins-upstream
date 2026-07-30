## Description: <br>
A tax compliance assistant for offshore trusts and cross-border family wealth that helps users structure self-checks, assess personal income tax obligations, review CRS and anti-avoidance considerations, and prepare practical compliance guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax-compliance practitioners use this skill to ask offshore-trust and cross-border wealth tax questions, run structured compliance self-checks, identify risk areas, and draft practical remediation or reporting guidance. Users should verify time-sensitive tax conclusions against official sources and qualified professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive offshore-trust, beneficiary, tax-residency, or cross-border wealth details may be processed by remote services. <br>
Mitigation: Avoid entering unnecessary personal or confidential details, confirm that remote processing by mcp.aitaxs.top is acceptable, and use anonymized scenarios where possible. <br>
Risk: The skill may store persistent API keys, client identifiers, and plaintext local logs. <br>
Mitigation: Review local files before and after use, protect the local user profile, and rotate or remove stored credentials when they are no longer needed. <br>
Risk: Running setup code can change MCP client configuration files. <br>
Mitigation: Do not run config/init_agent.py unless configuration changes are intended; review backups and generated MCP entries before continued use. <br>
Risk: Tax policy guidance can be time-sensitive and jurisdiction-specific. <br>
Mitigation: Verify conclusions against current official tax authority materials and consult qualified tax or legal professionals before filing or restructuring assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Offshore trust self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, workflow links, and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call or configure remote MCP services for policy Q&A, risk checks, tax calculations, and knowledge-base lookup; offline fallback guidance is available for limited scenarios.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
