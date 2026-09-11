## Description:

Turn a GitHub pull request into a code-change explainer video built from the diff, commits, and changed files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn a GitHub pull request into a narrated HyperFrames video that explains a changelog, feature reveal, fix, or refactor walkthrough.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches pull request data and may use GitHub or media-provider credentials.

Mitigation: Use limited-scope credentials and avoid sensitive private pull requests unless the run is isolated and access is approved.

Risk: The skill runs mutable HyperFrames tooling, installs registry blocks, and can update global skills.

Mitigation: Sandbox the run and pin, update, or pre-vet the CLI, skills, and registry blocks before deployment.

Risk: The skill processes untrusted pull request text with broad agent authority.

Mitigation: Review generated plans, scripts, commands, and files at the documented gates before rendering or publishing output.

## Reference(s):

- [Skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)
- [Code vocabulary](references/code-vocabulary.md)
- [Cut catalog](references/cut-catalog.md)
- [Motion language](references/motion-language.md)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project workflow that can culminate in rendered video output.]

## Skill Version(s):

1.0.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
