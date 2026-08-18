## Description:

Manages a paper-ingestion workflow from DOI, arXiv, or PDF input through metadata extraction, Markdown draft creation, value assessment, deep-reading notes, review, and repository commit/push.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangzw928](https://clawhub.ai/user/wangzw928)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to convert DOI, arXiv, or PDF paper inputs into organized Markdown notes, value assessments, deep-reading supplements, review questions, and paper-library index updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can modify a paper repository and push changes to its remote without a clear approval gate.

Mitigation: Require manual confirmation before commit and push, and review git status plus diffs before allowing repository changes.

Risk: The workflow stages changes broadly with git add -A, which can include unrelated files.

Mitigation: Stage only the intended paper note and index files rather than the entire working tree.

Risk: The workflow invokes an external Kimi Code CLI with broad workspace access.

Mitigation: Add a manual confirmation step before Kimi invocation and restrict the added workspace directory to the minimum repository path needed for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangzw928/skills/paper-reader)
- [Publisher profile](https://clawhub.ai/user/wangzw928)
- [DOI resolver](https://doi.org/)
- [arXiv API](http://export.arxiv.org/api/query)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces paper notes, value assessments, deep-reading supplements, review questions, status labels, and completion notices for a paper repository workflow.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
