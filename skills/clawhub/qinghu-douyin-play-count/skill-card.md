## Description:

Looks up the play count of a Douyin video from its link using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin creators and analysts use this skill to check the play count of a specific video by supplying its link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions may install or upgrade an unpinned Node/qhkit package on the host.

Mitigation: Preinstall a reviewed, pinned qhkit version; avoid persistent PATH changes unless needed.

Risk: The lookup requires a Qinghu API token configured on the host.

Mitigation: Use a token you are comfortable providing and review credential setup before running the skill.

Risk: Play-count lookups consume paid Qinghu credits, with no published base price in the skill.

Mitigation: Check the quoted credit cost and approve paid calls before they run; report actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-douyin-play-count)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Brief answer with the video play count and any credits charged]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the actual Qinghu credit charge when a paid lookup is made.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
