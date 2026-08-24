## Description:

Harness Dev Standards provides quality gates, checklists, remediation guidance, and shell scripts for reviewing TypeScript, JavaScript, and Node.js project readiness before delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-acheng](https://clawhub.ai/user/ai-acheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and small teams use this skill before delivery to run quality checks, apply review checklists, and receive remediation guidance for TypeScript and JavaScript projects, especially Next.js, Node.js, and React library work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages automatic code, dependency, and environment changes without enough user control.

Mitigation: Require explicit user approval before dependency changes, source edits, npm audit fix, global package installation, .env edits, or terminating processes; review diffs before applying changes.

Risk: Bundled scripts can install depcheck globally and run npm audit, npx tsc, npx eslint, and npm run build in the active project.

Mitigation: Run scripts only from the intended project root, review package manager effects before accepting fixes, and keep secret values out of command output and logs.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/AI-aCheng/harness-dev-standards)
- [ClawHub skill page](https://clawhub.ai/ai-acheng/skills/harness-dev-standards)
- [Standards reference](references/standards.md)
- [Delivery checklist](references/checklist.md)
- [Remediation guide](references/remediation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command snippets and checklist-style reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results; script outputs depend on the target project's package.json, TypeScript, ESLint, dependency, environment, and build setup.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
