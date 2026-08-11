## Description:

AI Delivery Spec is a requirement management skill for humans and AI agents, covering clarification, product contracts, prototypes, change tracking, and evidence-based acceptance for reliable delivery across ToC, ToB, and ToG projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Product managers, business stakeholders, developers, testers, and AI coding agents use this skill to turn ideas, existing systems, PRDs, prototypes, changes, and acceptance evidence into right-sized, traceable requirement artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is broad and may be invoked automatically for requirement-like tasks.

Mitigation: Install it only when the user wants a broad requirements and PRD workflow, and keep each run scoped to the requested target stage.

Risk: Bundled local Python gates can read and write requirement artifacts and inspect repository state for validation hashes.

Mitigation: Run the gates only inside project workspaces where local artifact reads, writes, and repository inspection are acceptable.

Risk: Static validation can be mistaken for business, browser, regulatory, implementation, or customer acceptance.

Mitigation: Treat gate output as structural evidence only; review the not-proven items and require domain, runtime, implementation, and customer evidence where those claims matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Stages reference](references/stages.md)
- [Lifecycle reference](references/lifecycle.md)
- [Specification reference](references/specify.md)
- [Prototype reference](references/prototype.md)
- [Change and acceptance reference](references/change-acceptance.md)
- [Tool adapters reference](references/tool-adapters.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, YAML, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured sidecar files and local validation outputs; static gate PASS does not prove business correctness, runtime behavior, or customer acceptance.]

## Skill Version(s):

5.4.5 (source: changelog, released 2026-08-10; server release version 5.4.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
