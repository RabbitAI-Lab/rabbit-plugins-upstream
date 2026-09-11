## Description:

Generates realistic, dialogue-driven short-drama video clips from a script beat or scene description using the Ofox video API and Seedance 2.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agent users use this skill to turn one dialogue-heavy script beat into a realistic short-drama video clip with a brief, structured prompt, cost estimate, job submission, polling, download, and cost report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an unpinned external core package that later uses OFOX_API_KEY for paid Ofox jobs.

Mitigation: Review the external ofox-video-core code and install it from a trusted pinned revision before exposing OFOX_API_KEY.

Risk: The skill can submit paid video-generation jobs if an agent proceeds without careful approval.

Mitigation: Use the documented dry-run and approval gate, set an explicit output directory, and confirm the quoted prompt and cost before any job is submitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-short-drama)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-short-drama)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured prompts, approval tables, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid Ofox video jobs after user approval and download generated video files through the external core workflow.]

## Skill Version(s):

1.11.1 (source: server release evidence, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
