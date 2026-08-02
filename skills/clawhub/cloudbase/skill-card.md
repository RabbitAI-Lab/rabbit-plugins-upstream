## Description: <br>
CloudBase helps agents develop, design, build, deploy, debug, migrate, and troubleshoot CloudBase projects across web, WeChat Mini Program, mobile, database, cloud function, CloudRun, storage, AI model, AI agent, operations, and specification workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route CloudBase work to the right reference material, prepare backend resources, implement application features, and review CloudBase-specific changes before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled examples may lead to insecure authentication, public access, credential handling, logging, or deployment behavior if copied directly into production. <br>
Mitigation: Review generated steps before execution, add least-privilege access control, redact secrets from logs, and adapt examples to production security requirements. <br>
Risk: CloudBase management actions can affect the wrong environment when EnvId values are implicit or ambiguous. <br>
Mitigation: Require explicit EnvId selection and resolve aliases to canonical EnvId values before API calls, deployments, deletions, or endpoint changes. <br>
Risk: API keys, public endpoints, custom AI endpoints, deployments, and deletion steps can expose data or change live resources. <br>
Mitigation: Require user review and approval for those actions and apply privacy notices, access control, and least-privilege checks before release. <br>


## Reference(s): <br>
- [ClawHub cloudbase skill page](https://clawhub.ai/binggg/skills/cloudbase) <br>
- [CloudBase main skill raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [CloudBase database security rules](https://docs.cloudbase.net/database/security-rules) <br>
- [CloudBase cloud function security rules](https://docs.cloudbase.net/cloud-function/security-rules) <br>
- [CloudBase storage security rules](https://docs.cloudbase.net/storage/security-rules) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, configuration steps, and review notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include CloudBase environment identifiers, deployment steps, API calls, and review findings that require user approval before execution.] <br>

## Skill Version(s): <br>
1.92.35 (source: ClawHub release metadata; bundled frontmatter version: 2.25.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
