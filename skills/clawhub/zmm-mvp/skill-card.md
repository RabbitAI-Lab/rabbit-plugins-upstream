## Description:

This skill turns a creator's topic fragment into plain-text X test posts, records the test, and uses engagement data to decide whether the idea should advance to video, expand into long-form writing, or be retired.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent knowledge creators and creator-supporting agents use this skill to validate uncertain topic ideas with low-cost X text posts before investing time in video or long-form content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local creator reference material, memories, and historical X performance data from the configured workspace.

Mitigation: Review the referenced vault and archive paths before first use, and remove or isolate sensitive material that should not be available to the agent.

Risk: The workflow can save drafts, update tracking files, move published drafts, write learned preferences, and overwrite the clipboard.

Mitigation: Run it only in the intended creator workspace and review generated files and clipboard contents before publishing or sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-mvp)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and plain-text X post drafts; helper script output is shell text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write draft, pipeline, memory, and clipboard state in the user's configured vault.]

## Skill Version(s):

0.2.1 (source: server release evidence; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
