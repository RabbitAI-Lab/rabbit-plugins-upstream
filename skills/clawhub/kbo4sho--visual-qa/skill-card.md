## Description:

Visual regression testing pipeline for web applications that captures baseline screenshots, compares new builds using pixel-level diffing, and gates deployments based on visual similarity thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kbo4sho](https://clawhub.ai/user/kbo4sho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to capture baseline screenshots, compare new app builds across pages and viewports, and fail CI or deployment gates when visual changes exceed configured thresholds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project config or CLI server values can run local shell commands.

Mitigation: Use only trusted repositories or isolated CI/container environments, and review every .visual-qa.json server value before running the skill.

Risk: Saved screenshots and diff images can expose sensitive application data.

Mitigation: Treat visual artifacts as sensitive, limit access to artifact directories, and avoid capturing private or secret-bearing pages unless approved.

Risk: Updating baselines with a destructive remove command can delete the wrong target if the path is not verified.

Mitigation: Verify the exact baseline path before deletion and review baseline changes under version control before accepting them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kbo4sho/skills/visual-qa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create PNG screenshots and diff images when its bundled scripts are run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
