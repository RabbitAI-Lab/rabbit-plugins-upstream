## Description:

Project initialization toolkit that analyzes project structure and configuration to generate a CONTRIBUTING.md guide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to inspect project configuration and produce a CONTRIBUTING.md guide that reflects detected setup, style, build, commit, and monorepo details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases may invoke the skill during general project initialization or contribution-guide requests.

Mitigation: Review when the skill is invoked and confirm the generated CONTRIBUTING.md before accepting it.

Risk: Generated contribution guidance may be misleading if project configuration is incomplete or multilingual expectations are not obvious from repository files.

Mitigation: Check the generated guide against project conventions, especially language choice, build commands, lint settings, and overwrite decisions.

## Reference(s):

- [Contributing Generator Guide](contributing.md)
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/repo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a CONTRIBUTING.md file only after overwrite confirmation when one already exists.]

## Skill Version(s):

0.3.3 (source: ClawHub release metadata and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
