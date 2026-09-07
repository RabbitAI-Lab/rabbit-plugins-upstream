## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant review, fix, validate, and re-review code over multiple rounds until the requested quality goal converges. It also supports defensive-programming workflows for normal coding tasks by adding pre-check, post-check, and invariant gates around edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-autonomy code edits, run configured validation commands, and use git, which can affect a repository beyond a single response.

Mitigation: Install and invoke it only in repositories where autonomous edits are acceptable, keep validation commands explicit, and review generated diffs before accepting or publishing changes.

Risk: Security evidence notes conflicting Git workflow instructions that could publish changes unexpectedly.

Mitigation: Treat merge and push as manual steps, regardless of documentation wording, and review any generated commits before publishing.

Risk: Security evidence flags a documented curl-to-bash harness install path as unsafe.

Mitigation: Avoid curl-to-bash installation paths and prefer package-manager or checked-release installation flows with checksum verification.

Risk: Personalization notes and project context files may capture sensitive project details if users include them.

Mitigation: Keep secrets out of personalization notes, generated project context, and review artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Release notes](RELEASE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code edits, configuration snippets, and validation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit files, run configured validation commands, and use git when invoked with write-capable modes.]

## Skill Version(s):

3.2.1 (source: frontmatter, pyproject.toml, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
