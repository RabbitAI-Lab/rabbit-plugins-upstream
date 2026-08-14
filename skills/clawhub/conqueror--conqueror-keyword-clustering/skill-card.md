## Description:

Group keywords into page-level clusters and map each cluster to an existing or new page, flagging cannibalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conqueror](https://clawhub.ai/user/conqueror)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners and content teams use this skill to turn keyword lists, saved keyword sets, Search Console data, or ranked domain keywords into page-level clusters and page recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword clusters or page mappings can be misleading if the project, source keywords, or Search Console context are wrong.

Mitigation: Confirm the project and keyword sources before running the workflow, and review clusters against SERP intent before acting on recommendations.

Risk: Cluster tags can be written back through save_keywords when the user approves that action.

Mitigation: Approve save_keywords only after reviewing the final clusters and confirming that the tag changes should be applied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conqueror/skills/conqueror-keyword-clustering)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown summary and table with page brief recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cluster counts, page creation and update recommendations, cannibalization notes, and optional save/tag suggestions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
