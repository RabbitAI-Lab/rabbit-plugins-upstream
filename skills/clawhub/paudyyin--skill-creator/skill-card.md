## Description:

Create, modify, and optimize agent skills with iterative evaluation, benchmark analysis, review workflows, and description refinement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to draft new skills, improve existing skills, run qualitative and quantitative evaluations, review outputs, and refine triggering descriptions before packaging a release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unsafe local side effects from review helpers that write evaluation workspaces, feedback files, temporary command files, and browser review pages.

Mitigation: Run without elevated privileges, review target paths before execution, prefer an isolated workspace, and confirm temporary command files and background viewers are stopped after use.

Risk: The security scan reports browser-injection risk when evaluating untrusted skills or outputs in the review helpers.

Mitigation: Prefer the static viewer or an unused random local port, and avoid reviewing untrusted skill outputs until HTML and JavaScript embedding uses context-safe escaping or non-executable JSON storage.

Risk: The skill can invoke the Claude CLI and run automated description-evaluation loops, which may consume tokens and operate under the current local authentication context.

Mitigation: Confirm the intended model, auth context, timeout, and eval set before running optimization loops, especially for third-party or untrusted skills.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/skill-creator)
- [JSON Schemas](references/schemas.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON structures, generated files, and local review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create evaluation workspaces, benchmark artifacts, feedback files, packaged .skill archives, and local or static HTML review pages.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
