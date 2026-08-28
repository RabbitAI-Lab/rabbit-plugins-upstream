## Description:

Helps AI video creators, advertising directors, and ecommerce content teams turn Seedance 2.0 video ideas into structured prompts, shot plans, model-routing choices, and AI-HIVE generation commands while avoiding unauthorized copying and unsupported claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External AI video creators, advertising directors, and ecommerce content teams use this skill to convert creative goals, product facts, scenes, motion, duration, and authorized reference assets into reviewable Seedance 2.0 prompts, scripts, shot lists, and AI-HIVE command workflows. The skill can also guide API-backed video generation after the user reviews parameters, routing, price snapshots, and media authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation calls may consume credits or create unwanted local files.

Mitigation: Review prompts, routing mode, price snapshots, and authorized media before submitting jobs; use --no-download or --output-dir to control downloads.

Risk: API keys could be exposed if pasted into prompts, logs, screenshots, or version control.

Mitigation: Use environment variables or the local config flow, keep example keys as placeholders, and avoid sharing real API keys in skill outputs.

Risk: Reference assets or commercial claims could be unauthorized, copied too closely, or unsupported.

Mitigation: Require rights to input media, preserve only abstract structure from references when authorization is unclear, and verify product facts before publication.

Risk: Generated video plans or outputs may not satisfy platform rules or business-performance expectations.

Mitigation: Run human review against channel requirements, avoid guarantees about traffic, ranking, sales, or approval, and validate each final asset before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/seedance-2-prompt-expert-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with inline shell commands, optional JSON briefs, and CLI output when scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE jobs, upload authorized media, poll asynchronous tasks, and download generated files to a user-selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
