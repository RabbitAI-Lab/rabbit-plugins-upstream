## Description: <br>
识别银行卡号、发卡银行和卡类型，使用 Luhn 算法校验卡号有效性。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xby-skill](https://clawhub.ai/user/xby-skill) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit a bank-card image URL or Base64 image payload to an OCR service, then receive the detected card number, issuing bank, card type, and Luhn validation result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bank-card images and OCR results are sent to a third-party service. <br>
Mitigation: Install only if you trust the Xiaobenyang service with this financial image data, and avoid uploading full card images unless necessary. <br>
Risk: The skill stores and reads an API key from the local environment. <br>
Mitigation: Use a limited-scope API key, keep .env out of version control, and rotate the key if it may have been exposed. <br>
Risk: The security guidance notes leftover Gaokao/search_schools references and generic API dispatch. <br>
Mitigation: Review or remove these leftovers before deployment so users can clearly understand the active behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xby-skill/skills/ocr-bank-card) <br>
- [Xiaobenyang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, api calls, configuration guidance] <br>
**Output Format:** [JSON API result summarized as text or Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and either an image URL or Base64-encoded image input.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
