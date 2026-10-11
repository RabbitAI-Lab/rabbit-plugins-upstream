## Description:

Searches Xiaohongshu (RedNote) posts by keyword, with optional filters for post type, publication time, and sort order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts search Xiaohongshu posts to explore topics, recent trends, and competitor content using keyword and optional result filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node and qhkit on the local machine.

Mitigation: Preinstall a reviewed, pinned qhkit version and approve environment changes before use.

Risk: Qinghu authentication can store an API token locally.

Mitigation: Provide credentials through a controlled environment variable instead of saving a token through the skill.

Risk: Search requests consume Qinghu credits, with charges varying by result count.

Mitigation: Check the current estimate and obtain user consent before paid calls or large result sets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-note-search)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown findings with an optional tabular results file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include filters, sample size, a short preview, and credits charged.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
