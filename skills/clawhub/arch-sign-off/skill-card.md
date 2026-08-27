## Description:

Append the Arch Linux sign-off line `btw, i use arch` to the bottom of articles in `ai-thoughts/docs/`, including English and Chinese counterparts, unless the user explicitly says not to.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill to apply a consistent Arch Linux sign-off to article drafts under `ai-thoughts/docs/`, while leaving files unchanged when the user opts out or when the target is outside the article directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may add the sign-off to article content where the author does not want it.

Mitigation: Tell the agent explicitly not to apply the sign-off for that article; the skill procedure treats user opt-out as authoritative.

Risk: The sign-off should not be added outside `ai-thoughts/docs/` or to repository metadata files.

Mitigation: Verify the target path before applying the skill and leave READMEs, `articles.yaml`, and files outside `ai-thoughts/docs/` unchanged.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell command and file edit]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify the target article file by appending one final sign-off line; leaves files unchanged when the sign-off already exists or the user opts out.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
