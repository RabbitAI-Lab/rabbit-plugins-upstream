## Description:

This skill provides a Twitter/X operations SOP for AI agents to help run owned accounts with onboarding, content-pool tracking, pre-publish checks, posting controls, daily logs, and weekly reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gingiris-1031](https://clawhub.ai/user/gingiris-1031)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, founders, marketers, and operators use this skill to help an agent manage an owned Twitter/X account without losing track of publishing state, content inventory, credential boundaries, or performance review tasks. It is intended for guided operations where public posts, logs, and reports remain subject to user approval and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated public posting can publish incorrect, unwanted, or brand-damaging content.

Mitigation: Require human approval before every post and enforce the skill's pre-publish checklist before using Twitter/X or Buffer publishing paths.

Risk: Credential-adjacent account handling can expose Twitter/X API keys, OAuth1 tokens, or Buffer tokens if they are written into working files.

Mitigation: Store credentials in a secret manager or protected environment variables, and keep credential values out of MASTER-STATUS.md, logs, reports, and chat transcripts.

Risk: Persistent operational logs can retain private conversations, account data, or unpublished content longer than intended.

Mitigation: Confirm the storage location before use, limit logs to necessary operational facts, and define deletion or retention rules for private or sensitive material.

Risk: Publishing decisions based on stale or unverified metrics can mislead readers.

Mitigation: Use the source-index and data-verification checks described by the skill, and remove or qualify numbers that cannot be traced to an approved source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gingiris-1031/skills/gingiris-twitter-agent-ops)
- [Publisher profile](https://clawhub.ai/user/gingiris-1031)
- [English README](artifact/references/en/README.md)
- [Japanese README](artifact/references/ja/README.md)
- [Korean README](artifact/references/ko/README.md)
- [Hugging Face dataset](https://huggingface.co/datasets/Gingiris/gingiris-twitter-agent-ops)
- [Gingiris tools](https://gingiris.tools/skills/)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown SOP with checklists, templates, status-file structures, and inline API command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance, tweet workflow prompts, daily log templates, weekly report templates, and publishing safety checks for an agent-managed Twitter/X workflow.]

## Skill Version(s):

2.0.2 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
