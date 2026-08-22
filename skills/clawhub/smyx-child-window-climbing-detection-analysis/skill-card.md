## Description:

Using fixed cameras aimed at windows or balconies, this skill analyzes child activity footage to detect climbing, leaning out, railing crossing, window-edge gripping, and other fall-risk behaviors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze consented window or balcony camera footage for child climbing, leaning, railing-crossing, and gripping behaviors. It returns structured detection results, alert levels, snapshots or report links, and history-query output for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home and child video may be sent to external analysis services.

Mitigation: Use only consented, non-sensitive test footage until the publisher documents production endpoints, retention practices, report access controls, and deletion procedures.

Risk: The skill can create and persist local user/account state and tokens for report access.

Mitigation: Run in an isolated workspace, review local data storage and token handling before use, and remove local/cloud records after testing when possible.

Risk: Child-safety alerts may be incomplete, delayed, or wrong and should not replace supervision.

Mitigation: Treat outputs as auxiliary alerts and require adult review and direct supervision for any real child-safety scenario.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API error-code reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON structured analysis reports with alert fields and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, history-list queries, optional output files, and basic, standard, or json detail modes.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
