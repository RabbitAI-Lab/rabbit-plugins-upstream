## Description: <br>
Analyzes public Douyin creator videos, interaction patterns, representative content, and topic structure, then produces HTML, Markdown, and JSON reports; it is not for private accounts, favorites synchronization, or bypassing platform access controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tars1230](https://clawhub.ai/user/tars1230) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, researchers, and content strategists use this skill to inspect publicly accessible Douyin creator profiles, select representative videos, transcribe eligible samples, categorize content themes, and generate auditable insight reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may reuse an authenticated Douyin browser profile. <br>
Mitigation: Prefer a dedicated browser profile and avoid exposing cookies, profile paths, or private account data in prompts, logs, reports, or third-party actors. <br>
Risk: Selected public media URLs or audio may be sent to configured ASR providers. <br>
Mitigation: Use index mode when transcription or media upload is not acceptable, and confirm ASR provider configuration before running real collection. <br>
Risk: API keys and local environment files can expose credentials if handled carelessly. <br>
Mitigation: Keep keys in a trusted secret store, avoid untrusted .env files, and do not place credentials in source files, CLI arguments, fixtures, logs, or generated reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-creator-insight) <br>
- [Apify Douyin actors reference](references/apify-douyin-actors.md) <br>
- [Creator resolution playbook](references/creator-resolution-playbook.md) <br>
- [Data schema](references/data-schema.md) <br>
- [Failure playbook](references/failure-playbook.md) <br>
- [Report rubric](references/report-rubric.md) <br>
- [Sample report](docs/sample-report.md) <br>
- [DashScope API key documentation](https://help.aliyun.com/zh/model-studio/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Files] <br>
**Output Format:** [Markdown guidance plus generated HTML, Markdown, and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include collection status, transcript provider status, quality gate results, and partial-result markers when collection is capped or incomplete.] <br>

## Skill Version(s): <br>
1.2.3 (source: changelog, released 2026-08-01; server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
