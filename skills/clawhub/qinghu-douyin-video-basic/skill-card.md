## Description:

Retrieves basic Douyin video details from a video link, including creator, engagement, title, music, publication time, and image collections, but not view counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

People analyzing Douyin videos use this skill to look up a video's creator, engagement, title, music, publication time, and image collection from its link without requesting view counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup or upgrades may install Node.js or qhkit globally and change the local runtime environment.

Mitigation: Review installation and upgrade steps first; install vetted, pinned dependencies in a controlled environment and do not allow automatic shell startup changes.

Risk: Queries require a Qinghu API token and may consume paid credits.

Mitigation: Manage the token securely, check the estimated charge, and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-basic)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise prose or Markdown; a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits charged for paid calls; does not include video view counts.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
