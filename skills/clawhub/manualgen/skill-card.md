## Description:

ManualGen helps AI coding assistants analyze business workflows, extract project features, and generate user-facing operation manuals through a staged state-machine workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhou666](https://clawhub.ai/user/songzhou666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation teams use ManualGen to turn an existing software project into a structured user operation manual for operators, sales teams, and customers. The workflow explores the project, extracts features and APIs, analyzes workflows and data dependencies, asks for confirmation, and then writes and audits the manual.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can scan project code and create persistent workspace files from broad trigger phrases without a clear upfront consent step.

Mitigation: Use it only when you want the full manual-generation workflow, run it in a clean branch or disposable working tree, and confirm the project scope before allowing progression.

Risk: Generated conflict exports, histories, analysis, and manuals may contain sensitive project documentation.

Mitigation: Review .agent/harness and final manual outputs before committing or sharing, and treat generated artifacts as sensitive until reviewed.

Risk: Hands-off auto progression can continue through multiple stages and create or update many artifacts.

Mitigation: Keep auto_confirm disabled unless you deliberately want hands-off operation, and review generated files before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songzhou666/skills/manualgen)
- [Publisher profile](https://clawhub.ai/user/songzhou666)
- [Server-resolved GitHub source: songzhou666/ManualGen](https://github.com/songzhou666/ManualGen)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)
- [Privacy notice](artifact/privacy/privacy-notice.md)
- [Anti-patterns reference](artifact/references/anti-patterns.md)
- [Deep FAQ](artifact/references/faq-deep.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown files, Mermaid diagrams, structured progress text, and workspace status artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes persistent analysis and manual-generation artifacts under .agent/harness and documentation outputs such as docs/manualgen or a project user manual.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 5.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
