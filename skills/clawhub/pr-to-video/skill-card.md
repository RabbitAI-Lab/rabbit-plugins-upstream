## Description:

Turns a GitHub pull request into a code-change explainer video built from the PR diff, commits, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn GitHub pull requests into concise explainer videos for changelogs, feature reveals, fixes, and refactor walkthroughs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use GitHub CLI access and ingest PR text from untrusted authors.

Mitigation: Run it only on repositories and pull requests you are authorized to process, and review the PR source before allowing generated plans or scripts to drive work.

Risk: The workflow may contact GitHub, CDN, HeyGen, and media services and may use HeyGen or media credentials.

Mitigation: Confirm the authentication status and allowed service posture before running; use offline paths or avoid sensitive repositories when external service use is not permitted.

Risk: The workflow may update globally installed HyperFrames skills through unpinned npx commands.

Mitigation: Review the installed package and skill updates before use, prefer an isolated environment, and pin or pre-approve versions when required by organizational policy.

## Reference(s):

- [Story design - PR to narrative](references/story-design.md)
- [Visual design - PR-to-video per-frame shot method](references/visual-design.md)
- [Code vocabulary - code animation blocks](references/code-vocabulary.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker - PR-to-video delta](sub-agents/frame-worker.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/pr-to-video)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown plans and scripts, JavaScript/HTML project files, shell commands, configuration files, and rendered video artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project from a GitHub pull request and can include narration, background music, sound effects, contributor avatars, and a final MP4 render.]

## Skill Version(s):

1.0.31 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
