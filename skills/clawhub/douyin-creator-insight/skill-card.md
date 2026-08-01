## Description: <br>
Analyzes public Douyin creator video topics, engagement structure, and representative content, then outputs HTML, Markdown, and JSON reports without supporting private accounts or bypassing platform access controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tars1230](https://clawhub.ai/user/tars1230) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and content researchers use this skill to collect and review public Douyin creator pages, confirm creator identity, inspect topic patterns, and generate auditable reports for content analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can reuse an authenticated persistent browser profile to access public Douyin pages. <br>
Mitigation: Run it with a separate low-privilege browser profile and do not expose cookies, tokens, profile paths, or private account content in prompts, logs, scripts, or reports. <br>
Risk: Generated JSON, Markdown, and HTML reports can preserve broad raw public creator data. <br>
Mitigation: Store reports in a private task directory, avoid publishing raw outputs, and delete collected outputs when they are no longer needed. <br>
Risk: Apify actors are an explicit fallback and their schemas, pricing, quotas, and availability can change. <br>
Mitigation: Verify the current actor page and response schema before real runs, start with small samples, and provide credentials only through the host environment or secret store. <br>
Risk: Nickname search, CAPTCHA, private accounts, or ambiguous creator matches can produce unreliable or unauthorized collection attempts. <br>
Mitigation: Use stable public profile URLs, share links, or sec_uid values; stop on CAPTCHA or ambiguous results instead of auto-selecting or bypassing access controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tars1230/skills/douyin-creator-insight) <br>
- [Apify Douyin actors reference](references/apify-douyin-actors.md) <br>
- [Creator resolution playbook](references/creator-resolution-playbook.md) <br>
- [Data schema](references/data-schema.md) <br>
- [Report rubric](references/report-rubric.md) <br>
- [Failure playbook](references/failure-playbook.md) <br>
- [Security policy](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus generated HTML, Markdown, and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports identify actual collection and transcript sources; browser-mode reports mark transcript candidates as skipped when no transcription provider is configured.] <br>

## Skill Version(s): <br>
1.1.0 (source: changelog and ClawHub release evidence, released 2026-07-30) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
