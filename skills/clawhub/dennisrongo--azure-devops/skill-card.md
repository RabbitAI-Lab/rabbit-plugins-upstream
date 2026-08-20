## Description:

Azure DevOps helps agents use the az CLI to query Azure Boards work items, inspect work-item text and screenshots, publish branches, and create pull requests with configured project defaults.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to work with Azure DevOps projects: listing assigned or sprint work items, reading work-item details and attachments, and preparing pull requests that follow configured team defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Branch pushes, pull-request creation, reviewer assignment, and auto-complete settings can change real Azure DevOps project state.

Mitigation: Install only where Azure DevOps access is intended and require explicit confirmation before any branch push or pull-request mutation.

Risk: Incorrect Azure DevOps configuration could target the wrong organization, project, branch, reviewer, or az executable.

Mitigation: Review .claude/azure-devops.json before use, especially organization, project, targetBranch, requiredReviewers, and azPath.

Risk: Failed or zero-byte work-item attachment downloads could lead to unsupported claims about screenshot contents.

Mitigation: Treat unopened attachments as not viewed, report the exact download error or GUID, and avoid describing image contents unless the image was successfully opened.

Risk: Azure DevOps authentication or PAT scope gaps can block identity resolution and related API calls.

Mitigation: Report the missing scope named by the Azure DevOps error, retry only the specific corrected call once, and stop rather than cycling through unrelated command variants.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/azure-devops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Azure DevOps query results, work-item summaries, attachment download status, pull-request command sequences, and verification notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
