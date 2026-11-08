## Description:

Translate a single, explicitly chosen article from ai-thoughts/docs/ into Simplified Chinese and save it as a matching -zh-hans.md file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and repository contributors use the skill to create a Simplified Chinese Markdown version of one specified article. The user identifies the source and approves the output path before the skill writes a file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because several local references could not be resolved.

Mitigation: Review the referenced files and the complete skill before installing.

Risk: The skill writes a translated article to a file, which can create or replace content at the approved destination.

Mitigation: Confirm the chosen source article and output path, and check whether an existing translation would be overwritten, before approving the write.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/translate-to-zh-hans)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Simplified Chinese Markdown article in a same-name -zh-hans.md file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the article structure and code; adds English glosses for technical terms.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
