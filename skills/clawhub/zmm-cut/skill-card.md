## Description:

This skill guides an agent through a ChatCut workflow for turning 詹明明 talking-head footage into publishable Douyin videos with speech cleanup, 1.15x pacing, captions, and user-selected highlight keywords.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users and creator-workflow agents use this skill to edit a specific creator's recorded talking-head footage into a publishable short video timeline. It focuses on preserving the spoken script while cleaning fillers, pacing the cut, adding captions, and preparing post-publication transcript feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad video-editing requests and reads or writes configured vault memory for editing preferences and post-publish script feedback.

Mitigation: Deploy only where this account-specific ChatCut workflow is intended, review activation triggers, and confirm that vault memory access is appropriate for the user and workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, api calls, configuration]

**Output Format:** [Markdown guidance with ordered workflow steps, checkpoints, and ChatCut tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an editable ChatCut timeline by default; MP4 export is only requested after explicit user confirmation.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence; artifact frontmatter states 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
