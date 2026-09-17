## Description:

Iterate helps coding agents run multi-round, multi-dimension code review and fixing workflows, plus defensive incremental coding flows with onboarding, validation, and installer/update support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use Iterate to run systematic code quality, security, performance, and architecture review loops with automated fixes. They can also use its defensive mode for incremental coding tasks that need pre-checks, post-checks, invariant checks, and validation evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-autonomy operation can edit files, run git, execute configured validation commands, and persist into assistant skill directories.

Mitigation: Install only after review, prefer a pinned installer version or manual reviewed installation, and confirm the requested workflow scope before allowing edits or command execution.

Risk: Install and validation-command paths expose users to mutable remote code execution risks.

Mitigation: Avoid the curl-to-bash harness command and inspect project-provided iterate.config.yaml validation commands, especially entries using npx, npm exec, pnpm dlx, or similar package execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills specification](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, code edits, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit files and run configured validation commands; merge and push are opt-in and disabled by default.]

## Skill Version(s):

3.4.1 (source: SKILL.md frontmatter, pyproject.toml, npm-installer/package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
