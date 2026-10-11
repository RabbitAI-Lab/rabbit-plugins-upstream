## Description:

Searches Pixabay Music for royalty-free background tracks and returns track URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find royalty-free background music by style and retrieve track links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs are sent to dLazy and requests may consume account credits.

Mitigation: Avoid sensitive queries and review expected costs or use the documented dry-run option before calling the service.

Risk: The CLI can upload local files supplied as media paths and write downloaded assets when saving results.

Mitigation: Do not pass local file paths or use --save unless the user explicitly intends those actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with track URLs and metadata; CLI results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search accepts short English style keywords and optional duration and page-size filters.]

## Skill Version(s):

1.3.28 (source: server release metadata; skill files state 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
