## Description:

Audits a WorkBuddy models.json registry for free OpenAI-compatible chat models, live-tests configured providers, applies add/remove changes, and writes a dated Markdown audit report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[igenomed](https://clawhub.ai/user/igenomed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to keep a custom free-model registry current by discovering usable free chat models, removing entries that are confirmed paid or invalid, and producing a dated audit inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically edit models.json, a sensitive model registry that can contain plaintext API keys.

Mitigation: Back up models.json before running the skill and review the resulting additions or removals, especially removals caused by provider errors or access changes.

Risk: The skill reads stored provider API keys and uses them to make live test calls.

Mitigation: Run the skill only in trusted workspaces and rotate provider API keys periodically or after suspected exposure.

Risk: Network, VPN, or regional connectivity failures can affect live model checks.

Mitigation: Confirm required VPN or proxy connectivity before overseas-provider tests and avoid removing models solely because connectivity probes fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/igenomed/skills/free-model-auditor)
- [Platform audit knowledge base](artifact/references/platforms.md)
- [Audit report template](artifact/templates/audit_report.md)
- [Path resolver helper](artifact/references/resolve_paths.py)
- [Live test harness](artifact/references/test_harness.py)
- [Google AI Studio](https://aistudio.google.com)
- [NVIDIA Build](https://build.nvidia.com)
- [SenseNova](https://www.sensenova.cn)
- [Agnes AI](https://agnes-ai.cn)
- [BigModel](https://open.bigmodel.cn)
- [SiliconFlow](https://cloud.siliconflow.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON registry edits, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a dated audit report and daily log; may directly update models.json.]

## Skill Version(s):

1.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
