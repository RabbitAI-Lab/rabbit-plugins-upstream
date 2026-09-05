## Description:

YuanZao yotta-skill-creator helps agents generate release-ready yotta skill scaffolds, validate naming and structure, and optionally create self-use skill bodies without release artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to create new yotta-prefixed skill directories from a compliant scaffold, including metadata, documentation, installer files, references, and optional CLI test skeletons. It is intended for new skill creation rather than writing final skill content, publishing, or migrating existing skill directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled installers can copy the skill into multiple agent skill directories, including user-level directories when broad install flags are used.

Mitigation: Review installer behavior before installing, prefer an explicit --agent or --dir target, and avoid -g or --global unless installation into every listed agent is intended.

Risk: The packaged full scaffold appears incomplete because required hidden template files are absent, which can make full-mode creation fail self-check.

Mitigation: Run the generated scaffold self-check and verify the package contents before relying on full-mode output for release preparation.

Risk: Using an unpinned npm install can fetch a newer package version than the one reviewed here.

Mitigation: Pin the npm package version when installing in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skill-creator)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skill-creator)
- [CLI reference](references/cli-reference.md)
- [Scaffold structure](references/scaffold-structure.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated scaffold files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained by the selected scaffold mode; full mode includes release artifacts, while self-use mode omits release packaging files.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact files report 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
