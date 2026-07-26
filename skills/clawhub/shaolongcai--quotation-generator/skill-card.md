## Description: <br>
专业的报价单生成助手。根据用户上传的物料价格表和Excel报价模板，自动分析模板结构、匹配产品价格、计算总价，生成填充完整的报价单Excel。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaolongcai](https://clawhub.ai/user/shaolongcai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business operations teams use this skill to generate quotation Excel workbooks from their own material price lists and quotation templates. The skill helps analyze template structure, match products and models, calculate prices, and prepare a filled quotation file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wrong uploaded spreadsheet may be used as the quotation template when a template is not explicitly provided. <br>
Mitigation: Ask the user to identify or upload the intended material price list and quotation template before generating the quote. <br>
Risk: Ambiguous product names with multiple models can lead to incorrect quotation lines. <br>
Mitigation: Require model clarification using only products and models present in the uploaded material price list before filling the workbook. <br>


## Reference(s): <br>
- [报价数据规范](references/data-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Guidance] <br>
**Output Format:** [Excel workbook with concise text status or clarification prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided Excel or CSV price lists and Excel quotation templates, then writes a uniquely named filled quotation workbook.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
