## Description:

Paper Parse analyzes user-provided academic papers from PDFs or URLs and produces two reader-focused Markdown reports for researchers and general audiences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and students use this skill to read, analyze, and summarize academic papers they intentionally provide as PDF files or URLs. It helps produce a deeper researcher-facing analysis and a general-audience explanation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, execute, write, and URL-handling authority, which can affect local files or network resources beyond simple paper summarization.

Mitigation: Review the skill before installing, run it in a constrained workspace, and confirm file paths and URLs before allowing downloads, command execution, or report writes.

Risk: The security evidence marks the release as suspicious because the artifact describes broader automation behavior beyond paper analysis.

Mitigation: Use the skill only for academic papers intentionally provided by the user and avoid sensitive files, private documents, and internal URLs.

Risk: Generated paper summaries and figure descriptions can be incomplete or misleading if PDF extraction fails or the source paper is malformed.

Mitigation: Check the final report against the original paper, especially methods, statistics, figures, and conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/paper-parse)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, guidance]

**Output Format:** [Markdown reports with a concise text delivery summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a temporary analysis file and a final paper reading report when the host agent permits file writes.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
