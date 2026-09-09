## Description:

The skill helps WeChat Official Account operators and content teams research viral article trends, generate article drafts and titles, rewrite copy, check prohibited terms, design cover concepts, and diagnose account performance using RedFox-backed WeChat data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External WeChat operators, content creators, brand teams, MCN agencies, editors, and content strategists use this skill to turn RedFox trend data into publish-ready WeChat articles, title options, compliance checks, cover concepts, and account diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends WeChat article data, drafts, account diagnostics, and sensitive-word checks to RedFox-backed services.

Mitigation: Use it only with content intended for RedFox processing, and avoid submitting confidential drafts or private account data unless that processing is acceptable.

Risk: The skill requires a REDFOX_API_KEY for API-backed workflows.

Mitigation: Use a revocable key, keep it in environment configuration, and avoid hard-coding or sharing it in prompts, logs, code, or output files.

Risk: One title-query debug path can print request headers.

Mitigation: Avoid sharing debug logs and review logs for exposed credentials before storing or forwarding them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-creator)
- [RedFoxHub](https://redfox.hk)
- [README.en.md](README.en.md)
- [M1 API specification](references/m1_api_spec.md)
- [M5 prohibited word workflow](references/m5_prohibited_word_core_workflow.md)
- [M7 account diagnosis workflow](references/m7_core_workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown responses with tables, generated article copy, title lists, report guidance, shell commands, and optional HTML or text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; some workflows submit prompts, drafts, account data, or text for RedFox processing.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
