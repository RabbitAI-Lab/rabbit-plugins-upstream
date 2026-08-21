## Description:

Automates Coze customer-service bot deployment, including knowledge-base creation, document upload, bot configuration, API publication, regression testing, and listing-material generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhenwo1314](https://clawhub.ai/user/zhenwo1314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy and prepare customer-service agents for Coze-based commercial workflows. It is intended for creating or updating bots, uploading approved knowledge-base files, publishing an API connector, running regression checks, and preparing store submission materials.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill uses a Coze API token to create or update remote Coze datasets and bots and publish an API connector.

Mitigation: Use a least-privilege Coze token where possible, keep credentials scoped to the intended workspace, and review the bot and connector before publication.

Risk: Files from the selected knowledge-base directory are uploaded to Coze.

Mitigation: Point the knowledge-base directory only at reviewed, approved documents and exclude confidential files that should not leave the local environment.

Risk: Generated bot prompts and listing materials can affect compliance-sensitive customer-facing claims.

Mitigation: Review generated prompts, regression outputs, and store materials for the relevant business, advertising, medical, education, pricing, and refund constraints before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhenwo1314/skills/bot-publish)
- [Coze API endpoint](https://api.coze.cn)
- [Coze chat API endpoint](https://api.coze.cn/v3/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated file references, deployment identifiers, and test summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce bot_id, dataset_id, published version, regression-test summaries, listing copy, and review materials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
