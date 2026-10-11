## Description:

Collects comments on a Xiaohongshu (RedNote) post from its link, with optional sorting and replies, using the Qinghu data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and analysts collect comments and optional replies from a specified Xiaohongshu post to understand audience questions and feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic setup may install or upgrade Node and qhkit on the user's machine.

Mitigation: Use a managed environment with a reviewed, pinned qhkit installation; require approval before changing the toolchain.

Risk: The skill requires a Qinghu API token and invokes paid data calls with usage-dependent charges.

Mitigation: Protect the token, review the current cost estimate, and obtain user consent before paid calls or larger batches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-comments)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise summary with a small preview; tabular file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits charged for paid calls and may provide a local JSON result file for large responses.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
