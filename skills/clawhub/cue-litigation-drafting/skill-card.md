## Description:

A Cue-based legal drafting skill for litigation lawyers and legal teams that creates Chinese litigation document drafts from case facts, party positions, or opposing materials, with statute and case-reference support for lawyer review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal professionals and legal operations teams use this skill to draft Chinese litigation materials such as complaints, answers, appeal petitions, evidence objections, lawyer letters, agency statements, and evidence directories. The output is a draft aid and must be reviewed and revised by a licensed lawyer before filing or sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send case materials, credentials, and other sensitive legal information to a third-party Cue service.

Mitigation: Use only after verifying Cue service terms, access controls, retention behavior, and suitability for the confidentiality level of the matter.

Risk: The skill may write persistent local configuration containing a Cue API key.

Mitigation: Store credentials with least privilege, restrict local file access, and rotate or remove the key when the drafting task is complete.

Risk: The skill can install and execute code from a mutable external repository.

Mitigation: Review and pin the exact runner code before installation or execution, and avoid using the skill in privileged environments until that code has been vetted.

Risk: Generated legal drafts, statutes, and case references may be incomplete, outdated, or inaccurate.

Mitigation: Require review, citation checking, and final editing by a qualified lawyer before filing, sending, or relying on the draft.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-litigation-drafting)
- [Cue platform](https://cuecue.cn)
- [Cue playbook](https://cuecue.cn/playbook)
- [Cue API key management](https://cuecue.cn/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown legal drafts with optional Word document conversion guidance and local command execution steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are draft legal documents and operational guidance; generated legal authorities and case references require professional verification.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
