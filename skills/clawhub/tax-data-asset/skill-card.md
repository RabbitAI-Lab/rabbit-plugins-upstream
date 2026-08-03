## Description: <br>
Provides Chinese tax compliance guidance, self-check workflows, risk scanning, and report prompts for bringing data resources or data assets onto the books. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, compliance, and listing-readiness teams use this skill to assess data-asset accounting and tax differences, transfer or licensing tax treatment, R&D super-deduction classification, ownership compliance, valuation risk, and audit-question readiness. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Cloud processing by mcp.aitaxs.top may involve confidential tax, financial, or corporate data. <br>
Mitigation: Use the skill only with data approved for cloud processing, avoid unnecessary identifiers, and review the consent text before submitting self-check inputs. <br>
Risk: The skill may store persistent API keys, client identifiers, cache, or logs under local client storage and browser localStorage. <br>
Mitigation: Use separate work profiles for sensitive matters, restrict shared-machine access, and clear or rotate stored credentials when no longer needed. <br>
Risk: Fallback search can rely on open-web results when the remote service is unavailable. <br>
Mitigation: Treat fallback answers as preliminary and verify tax positions against official tax authority sources or professional review before acting. <br>
Risk: Optional setup code can write MCP client configuration when explicitly enabled. <br>
Mitigation: Do not run config/init_agent.py directly or set TAX_ENABLE_AUTOSETUP=1 unless local MCP client configuration changes are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-data-asset) <br>
- [Interactive data-asset tax self-check page](https://mcp.aitaxs.top/web/topic_workflow_data_asset.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, copied report text, JSON-like tool results, Python output, and local HTML workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can use cloud MCP tools for tax guidance and risk checks, with limited offline checklist/search fallback when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
