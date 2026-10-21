## Description:

Helps scholars revise academic manuscripts in Chinese or English through style checks, deterministic cleanup, integrity safeguards, and guided rewriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and academic authors use the skill to review manuscript style, clean up common writing artifacts, guide revisions, and check that key numbers and citations remain intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed processing bugs may affect edited drafts.

Mitigation: Keep the original, write edits to a separate file with -o, avoid aggressive mode and stdout/--quiet pipelines for edited text, and manually review every change and numerical warning even when verification passes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Project repository](https://github.com/docsor1212/paper-rewriter)
- [ModelScope mirror](https://modelscope.cn/skills/Docsor/paper-rewriter)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Guidance]

**Output Format:** [Revised manuscript text, structured command-line reports, and Markdown revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file outputs; format depends on the selected command and options. Review edits before use.]

## Skill Version(s):

4.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
