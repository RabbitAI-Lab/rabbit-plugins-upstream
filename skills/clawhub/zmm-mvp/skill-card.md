## Description:

Turns a creator's rough topic fragment into ready-to-post X text drafts, records the test pipeline, and uses real interaction data to decide whether the topic should become a Douyin video, a WeChat article, or be dropped.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to cheaply validate topic ideas on X before investing effort in videos or long-form articles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects access to local creator references, memory files, and a CSV used for voice calibration.

Mitigation: Review and constrain the referenced vault and data paths before use if they contain unrelated private material.

Risk: The workflow can write draft posts and testing pipeline records into the user's vault.

Mitigation: Review generated draft and pipeline files before treating them as publication-ready records.

Risk: The workflow can replace clipboard contents with finalized post text.

Mitigation: Confirm clipboard contents before pasting into X or any publishing surface.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-mvp)
- [ClawHub publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text X post drafts, Markdown draft records, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local draft and pipeline files and copy finalized post text to the clipboard when used as described.]

## Skill Version(s):

0.2.2 (source: server release metadata; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
