## Description: <br>
Provides a Twitter/X operations SOP for AI-assisted account management, including onboarding, source tracking, daily posting logs, weekly reports, pre-publish checks, and separate OAuth1 and Buffer publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gingiris-1031](https://clawhub.ai/user/gingiris-1031) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and growth teams use this skill to operate Twitter/X accounts with repeatable content planning, source verification, posting checklists, and performance reporting. It is most relevant when an agent drafts or schedules posts and the user needs safeguards for facts, cadence, credentials, and account-specific voice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide automated live posting and credential-based control of Twitter/X workflows. <br>
Mitigation: Require explicit human approval before every live post and restrict the agent to draft, checklist, and scheduling assistance unless posting authority is intentionally granted. <br>
Risk: API tokens or account-specific publishing credentials could be exposed or used with the wrong account. <br>
Mitigation: Keep OAuth1 and Buffer tokens in a secret store, never paste credentials into MASTER-STATUS.md, and verify the target account, credential set, and Buffer profile before use. <br>
Risk: Incorrect analytics or unsourced numbers in social posts could mislead readers. <br>
Mitigation: Require every numeric claim to have a traceable source and cross-check single-source traffic or analytics figures before publication. <br>
Risk: The package includes an internal account-specific reference file. <br>
Mitigation: Review references/weiyipei-ops.md before deployment or redistribution and remove private paths, account-specific details, or workflow assumptions that do not apply. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/gingiris-1031/skills/gingiris-twitter-agent-ops) <br>
- [English SOP reference](references/en/README.md) <br>
- [Japanese SOP reference](references/ja/README.md) <br>
- [Korean SOP reference](references/ko/README.md) <br>
- [Gingiris Hugging Face profile](https://huggingface.co/Gingiris) <br>
- [Gingiris tools](https://gingiris.tools/) <br>
- [Twitter API tweet endpoint](https://api.twitter.com/2/tweets) <br>
- [Buffer API update endpoint](https://api.bufferapp.com/1/updates/create.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklists, templates, operational tables, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce account operations logs, source indexes, schedules, tweet drafts, pre-publish checklists, and weekly reports.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter is 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
