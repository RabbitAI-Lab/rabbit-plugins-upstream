## Description:

Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, planners, and reviewers use this skill to stress-test plans or designs through a structured, one-question-at-a-time interview that resolves decision dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: For code-related design questions, the skill may inspect project files instead of asking the user.

Mitigation: Use it in workspaces where agent file reading is acceptable.

Risk: The skill's recommended answers may be incomplete or unsuitable for the user's actual constraints.

Mitigation: Treat recommendations as review prompts and confirm decisions before implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/grill-me)
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/grill-me)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or Markdown conversational prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive; asks one question at a time and includes a recommended answer.]

## Skill Version(s):

0.1.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
