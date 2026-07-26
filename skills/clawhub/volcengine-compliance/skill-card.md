## Description: <br>
Volcengine Compliance helps agents recommend Volcengine Config compliance baselines, summarize current compliance posture, and guide custom Rego rule creation when built-in baselines do not cover a request. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud security teams, and compliance operators use this skill to select Volcengine compliance baselines, review account compliance reports, and prepare custom Config rules for uncovered checks. Write actions are limited to user-confirmed baseline deployment, recorder enablement, or custom rule registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed write actions can change Volcengine account state by deploying conformance packs, enabling the configuration recorder, or registering custom rules. <br>
Mitigation: Use dry-run output first, explain the intended account changes to the user, and require explicit confirmation before adding --confirm or registering rules. <br>
Risk: Generated compliance reports and local artifacts may contain sensitive account inventory details. <br>
Mitigation: Store report files only in trusted locations, protect or delete them after review, and redact resource identifiers before sharing outside the intended audience. <br>
Risk: Cloud credentials or session tokens may be exposed if copied into reports, command output, or user-facing summaries. <br>
Mitigation: Never print AK, SK, Authorization headers, or session tokens; use scoped credentials and rely on the Volcengine CLI authentication path. <br>
Risk: Custom Rego rules can produce misleading compliance results when resource schemas or field values are guessed. <br>
Mitigation: Resolve supported resource types, inspect schema or real resource snapshots, test representative compliant and non-compliant cases, and rely on server-side compilation before registration. <br>
Risk: Compliance overviews may be incomplete while the recorder is disabled or asynchronous evaluation is still pending. <br>
Mitigation: Confirm recorder status and rerun overview after rules or conformance packs have had time to evaluate resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-compliance) <br>
- [Authentication and prerequisites](references/auth.md) <br>
- [Compliance recommendation](references/recommend.md) <br>
- [Compliance overview](references/overview.md) <br>
- [Deploying compliance packs](references/apply.md) <br>
- [Writing custom Config rules](references/writing-config-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown and JSON guidance, with optional generated Markdown, CSV, and JSON compliance report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendation and overview paths are read-only; deployment, recorder enablement, and custom rule registration require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
