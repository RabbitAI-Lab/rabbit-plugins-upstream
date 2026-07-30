## Description: <br>
Twitter/X Agent Operations is an SOP skill for AI-assisted Twitter/X account management, including account context collection, content sourcing, scheduling, pre-publish checks, posting workflows, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gingiris-1031](https://clawhub.ai/user/gingiris-1031) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and growth teams use this skill to run AI-assisted Twitter/X operations with source-backed drafting, cadence control, pre-publish checks, and post-publish reporting. It is intended for authorized accounts where the operator can review public posts and manage platform credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports live public posting to Twitter/X and Buffer-backed accounts. <br>
Mitigation: Use draft or manual approval mode for posts unless the account owner has explicitly authorized automated publication. <br>
Risk: OAuth, Buffer, and browser-session credentials may be exposed if stored in operating logs or shared status files. <br>
Mitigation: Store credentials in a secrets manager or environment variables, and keep MASTER-STATUS.md, tweet logs, and reports free of secrets. <br>
Risk: The artifact includes an internal @WeiYipei operations reference marked as not for public release. <br>
Mitigation: Remove references/weiyipei-ops.md before redistribution or deployment outside the intended private environment. <br>
Risk: Automated content generation can publish inaccurate metrics, repeat topics, or drift from the account owner's voice. <br>
Mitigation: Require source-backed SOURCE-INDEX entries, pre-publish red-line checks, duplicate checks, and regular review of generated weekly reports. <br>
Risk: Durable local analytics records can contain account activity and performance history. <br>
Mitigation: Limit access to tweet logs, weekly reports, and status files, and retain only the operational data needed for the account workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gingiris-1031/skills/gingiris-twitter-agent-ops) <br>
- [English SOP reference](references/en/README.md) <br>
- [Japanese SOP reference](references/ja/README.md) <br>
- [Korean SOP reference](references/ko/README.md) <br>
- [Gingiris playbooks](https://gingiris.tools/skills/) <br>
- [Hugging Face publisher page](https://huggingface.co/Gingiris) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with templates, checklists, status files, and API command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce public post drafts, operating logs, schedules, reports, and credential-handling instructions for Twitter/X and Buffer workflows.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
