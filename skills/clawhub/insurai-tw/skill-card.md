## Description: <br>
Uses the InsurAI Agent API for Republic of China (Taiwan) personal insurance planning, product search and recommendation, occupation lookup, policy review, coverage-gap analysis, and contract or premium document retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jrsoft-insurai](https://clawhub.ai/user/jrsoft-insurai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and insurance-focused agents use this skill to handle Taiwan personal insurance questions by applying scope rules, gathering consent, calling InsurAI API endpoints, and summarizing planning, product, document, and policy-review results. <br>

### Deployment Geography for Use: <br>
Republic of China (Taiwan) <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive insurance, financial, health-related, or identity data may be included in planning and policy review inputs. <br>
Mitigation: Obtain consent before the first API call, submit only the minimum necessary fields, and redact national IDs, contact details, payment data, medical records, and unrelated policy pages. <br>
Risk: Policy images or PDFs may be processed by external OCR or document tools before this skill analyzes extracted text. <br>
Mitigation: Confirm the external processor's privacy terms and send only extracted text needed for the task to InsurAI. <br>
Risk: API-derived insurance outputs may be incorrect or incomplete if unsupported geography, unsupported insurers, OCR errors, or API errors are ignored. <br>
Mitigation: Apply Taiwan scope and rejection rules, validate insurer and product codes through the API, cross-check OCR-derived policy data, and stop on documented API errors. <br>


## Reference(s): <br>
- [InsurAI Taiwan Dev Business Rules](references/insurai-rules.md) <br>
- [InsurAI REST API Endpoint Contract](references/insurai-api-spec.md) <br>
- [insurai_api.py Script Reference](references/insurai-api-script.md) <br>
- [Policy Review and Coverage Gap Workflow](references/policy-review-workflow.md) <br>
- [InsurAI](https://insurai.com.tw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and summarized API-derived results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires INSURAI_API_KEY; sends minimum necessary user-provided insurance details to the configured HTTPS InsurAI endpoint after consent.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter, VERSION, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
