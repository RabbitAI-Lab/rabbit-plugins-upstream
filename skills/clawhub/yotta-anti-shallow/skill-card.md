## Description:

Helps agents approach complex tasks with analysis, clear uncertainty, and a final self-check instead of superficial answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users apply this skill to tasks needing careful reasoning, root-cause analysis, verification, and candid reporting of uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The behavior rules may activate across many complex tasks and add process where it is not wanted.

Mitigation: Install only if you want persistent quality rules; review the scope and disable optional process rules when appropriate.

Risk: Running the installer can write to agent skill directories, including multiple agents with global installation.

Mitigation: Prefer a pinned version or reviewed local copy, run --dry-run first, confirm the target directory, and avoid -g unless needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [Project homepage](https://github.com/YottaMeta/yotta-anti-shallow)
- [Skill FAQ](references/faq.md)
- [Complex-task walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an analysis, confidence statement, and self-check; does not execute code or replace testing or human review.]

## Skill Version(s):

1.4.2 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
