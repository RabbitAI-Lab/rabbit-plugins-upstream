## Description: <br>
私域专家团 · 马甲实战版 is a Chinese private-domain marketing operations assistant that routes `/siyu` work across content, group messaging, welcome scripts, business diagnosis, market research, local customer archives, and report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External operators, consultants, and business users use this skill to choose the next private-domain marketing action, draft compliant Chinese customer-facing materials, run evidence-gated vendor or market checks, and preserve or summarize customer work across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save, restore, and report from local plaintext customer archives under `~/.siyu/`. <br>
Mitigation: Use explicit archive commands, review stored files before and after use, and avoid saving personal, financial, or confidential customer details without consent and a retention plan. <br>
Risk: Generated reports can merge multiple customer archives and may reproduce sensitive or stale information. <br>
Mitigation: Review the source archives and generated report before sharing, remove sensitive details, and verify that retained conclusions still apply. <br>
Risk: Private-domain marketing outputs can create compliance risk if they include unsupported claims, prohibited wording, or platform-rule-sensitive actions. <br>
Mitigation: Use the included compliance checks and require current evidence for vendor, product, price, policy, platform-rule, and company-status claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-siyu) <br>
- [New user guide](artifact/references/新手教程.md) <br>
- [Full setup guide for business owners](artifact/references/整盘怎么搭-老板版.md) <br>
- [Module index](artifact/modules/index.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with occasional inline shell commands or structured snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are primarily Chinese, task-routed, and may include local file paths for customer archives or reports.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter, README.md, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
