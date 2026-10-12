## Description:

Guides agents to create or edit custom HyperFrames video compositions for multi-scene pieces, montages, title cards, and footage remixes when no specialized workflow fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan, build, and revise custom video compositions, including branded reels, multi-scene stories, loops, and footage edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs and updates an unpinned external CLI, so its behavior may change between runs.

Mitigation: Review before installing and prefer a pinned or locally vetted HyperFrames CLI.

Risk: The workflow may query hosted catalogs, use authenticated media providers, and write project files.

Mitigation: Check provider access and review generated project files and the final preview before rendering.

## Reference(s):

- [General Video skill release on ClawHub](https://clawhub.ai/heygen-com/skills/general-video)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions, Shell commands, Files]

**Output Format:** [Markdown guidance and video project files (HTML and JSON); rendered video after approval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires project checks and preview approval before rendering.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
