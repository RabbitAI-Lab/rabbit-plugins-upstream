## Description: <br>
Generates Chinese business-plan deliverables through a concise question flow, dynamic financial and feasibility analysis, and an optional local PowerPoint generator. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Entrepreneurs, founders, and business advisors use this skill to collect core project information, assess market, financial, feasibility, valuation, and risk factors, and prepare business-plan materials for fundraising, technology transfer, market-entry planning, or strategy work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local PPT generation script can install python-pptx automatically, modifying the user's Python environment. <br>
Mitigation: Review the script before use and install python-pptx explicitly in a controlled environment, or remove the auto-install fallback. <br>
Risk: Business-plan inputs may include sensitive strategy, fundraising, financial, and team information. <br>
Mitigation: Use a trusted local workspace, avoid unnecessary sharing of input JSON or generated PPTX files, and choose an output path appropriate for sensitive business data. <br>
Risk: Generated financial projections, feasibility scores, and valuation ranges may be incomplete or misleading if user inputs are speculative. <br>
Mitigation: Treat outputs as planning drafts and have financial, legal, and market assumptions reviewed by qualified stakeholders before external use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golngod/skills/wanpaike-opc-business-plan) <br>
- [Publisher profile](https://clawhub.ai/user/golngod) <br>
- [OPC-BP Feasibility Radar](references/OPC-BP可行性雷达.md) <br>
- [OPC Technology Enterprise Valuation Model](references/OPC科创企业估值模型.md) <br>
- [Financial Forecast Model](references/财务预测模型.md) <br>
- [Market Analysis Template](references/市场分析模板.md) <br>
- [Business Model Canvas](references/商业模式画布.md) <br>
- [Risk Analysis Framework](references/风险分析框架.md) <br>
- [Coze platform](https://coze.cn) <br>
- [OPC platform](https://opc.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance, structured JSON input, shell command examples, and generated PPTX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a 15-page business-plan presentation, a short content summary, feasibility scoring, valuation analysis, and risk analysis when sufficient user inputs are provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter describes v2.0.0 behavior) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
