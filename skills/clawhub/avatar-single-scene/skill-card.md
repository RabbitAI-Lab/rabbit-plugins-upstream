## Description:

Use when someone wants one polished host-on-camera beat - a speaking person with intake and approval gates before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and generate a single host-on-camera avatar clip with explicit intake, still-image approval, and clip approval gates before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup asks users to install several remote skills through unpinned npx commands.

Mitigation: Review install commands before use and prefer pinned versions or verified commits for the skills CLI and PrunaAI skill references.

Risk: The workflow may upload portraits, audio, scripts, prompts, and generated asset URLs to the provider.

Mitigation: Confirm that the user is comfortable sharing those assets with the provider before generation.

Risk: Paid generation calls could run before review if approval gates are skipped.

Mitigation: Keep the plan, still, and clip approval gates enabled before any paid generation call.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, API parameter names, and manifest requirements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an agent workflow for intake, approval gates, still generation or upload, avatar generation, and manifest capture.]

## Skill Version(s):

1.0.13 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
