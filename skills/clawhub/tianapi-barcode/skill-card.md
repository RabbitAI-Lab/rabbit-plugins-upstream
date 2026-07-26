## Description: <br>
通过商品条形码查询品牌、规格、厂商、分类等商品基础信息。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to look up product details from a 13-digit barcode through the TianAPI Barcode API, then present fields such as product name, brand, specification, category, manufacturer, and image URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The TianAPI key may be exposed through command-line usage, displayed URLs, shared output, or a committed .env file. <br>
Mitigation: Use a low-privilege key, prefer environment-variable configuration, avoid command-line key arguments, redact key-bearing URLs before sharing, and keep scripts/.env out of shared or committed workspaces. <br>
Risk: The helper script is reported as malformed and may fail until corrected. <br>
Mitigation: Review and test scripts/fetch_barcode.py before relying on it, and align the documented environment variable with the script's implementation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-barcode) <br>
- [TianAPI Barcode API documentation](https://www.tianapi.com/apiview/138) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and formatted barcode lookup results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI barcode API key configured outside shared or committed files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
