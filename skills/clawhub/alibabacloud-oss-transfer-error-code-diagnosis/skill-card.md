## Description:

Diagnoses Alibaba Cloud OSS upload and download failures by routing user-provided error codes, HTTP status values, and transfer context to catalog-backed root-cause directions and troubleshooting steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and support engineers use this skill to triage Alibaba Cloud OSS upload and download failures. It maps reported OSS error codes, HTTP statuses, and transfer context to root-cause categories, side attribution, and next troubleshooting steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Question-based runs can contact help.aliyun.com and write a persistent local documentation cache despite offline-only claims.

Mitigation: Review before installing in restricted or privacy-sensitive environments, and run only where public documentation access and local cache writes are acceptable.

## Reference(s):

- [Error Code Catalog](references/error-code-catalog.md)
- [Troubleshooting Playbook](references/troubleshooting-playbook.md)
- [Scope and Limitations](references/scope-and-limitations.md)
- [RAM Policies](references/ram-policies.md)
- [Alibaba Cloud OSS HTTP 403 Error Codes](https://help.aliyun.com/zh/oss/user-guide/http-403-error-code)
- [Alibaba Cloud OSS HTTP 400 Error Codes](https://help.aliyun.com/zh/oss/user-guide/http-400-error-code)
- [Alibaba Cloud OSS HTTP 404 Status Codes](https://help.aliyun.com/zh/oss/user-guide/http-status-code-404)
- [Alibaba Cloud OSS HTTP 503 Status Codes](https://help.aliyun.com/zh/oss/user-guide/http-status-code-503)
- [Alibaba Cloud OSS Error Response Parsing](https://help.aliyun.com/zh/oss/user-guide/overview-14)
- [Alibaba Cloud OSS Signature FAQ](https://help.aliyun.com/en/oss/developer-reference/faq-24)
- [Alibaba Cloud OSS Common Errors](https://help.aliyun.com/en/oss/user-guide/common-errors)
- [Alibaba Cloud OSS PutBucket Error Codes](https://help.aliyun.com/zh/oss/developer-reference/putbucket)
- [Alibaba Cloud OSS Usage Limits](https://help.aliyun.com/zh/oss/product-overview/limits)
- [Alibaba Cloud OSS Authorization Syntax and Elements](https://help.aliyun.com/zh/oss/user-guide/authorization-syntax-and-elements)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown response with script-derived diagnostic details and optional inline shell command.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnosis is driven by local script output; question-based runs may cite returned official Alibaba Cloud OSS documentation URLs.]

## Skill Version(s):

0.0.1 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
