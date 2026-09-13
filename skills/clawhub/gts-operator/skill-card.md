## Description:

GTS 多租户配置平台（表单+审批流）的 AI 原生操作员 skill，支持 AI Agent 通过自然语言完成租户注册、组织与人员维护、表单和工作流配置、业务单据发起、审批、查询导出，以及表单复用和模板共享。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dengkane](https://clawhub.ai/user/dengkane)

### License/Terms of Use:

MIT-0

## Use Case:

GTS tenant administrators and operators use this skill to manage forms, approval workflows, organization data, business records, approvals, exports, imports, and shared templates through conversational agent instructions backed by the live GTS HTTP API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists a 30-day bearer token in a local plaintext file.

Mitigation: Install only on a trusted, single-user machine, treat ~/.gts-operator.json as sensitive, and delete it when access is no longer needed.

Risk: The skill can perform real tenant-management actions with the authorized account's permissions.

Mitigation: Review requested operations carefully and require explicit confirmation for approval actions, tenant creation, exports, imports, template publishing, template installation, and template removal.

Risk: The template market is described as an unaudited public directory.

Mitigation: Preview templates before installation, relay warnings to the user, and confirm public publishing or removal actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dengkane/skills/gts-operator)
- [GTS API endpoint](https://www.geeyo.com/s/gts/api.php)

## Skill Output:

**Output Type(s):** [API Calls, Configuration, Guidance, JSON, Text]

**Output Format:** [Conversational text with HTTP API actions, JSON request and response details, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can persist an OAuth bearer token in ~/.gts-operator.json and can perform live tenant-management actions with the authorized account's permissions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
