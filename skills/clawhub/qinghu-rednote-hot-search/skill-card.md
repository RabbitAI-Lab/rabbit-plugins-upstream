## Description:

Retrieves the current Xiaohongshu (RedNote) hot-search ranking through Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to check current Xiaohongshu hot searches and identify potential topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update Node and qhkit and change the local environment.

Mitigation: Review installation steps first; prefer a preinstalled, pinned qhkit version.

Risk: A Qinghu API token is needed to make paid queries.

Mitigation: Use a scoped, revocable token and confirm the quoted cost before calling the paid tool.

Risk: Broad topic-finding requests may unintentionally trigger a paid hot-search lookup.

Mitigation: Confirm that the user wants Xiaohongshu hot-search data before invoking the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-hot-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary with key results; table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits used for paid queries.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
