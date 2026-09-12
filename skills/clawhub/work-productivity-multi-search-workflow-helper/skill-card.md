## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, artifacts, checklists, analyses, or implementation support for Multi Search Engine-style productivity work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn Multi Search Engine-style productivity needs into concrete plans, checklists, analyses, code changes, or adjacent workflow artifacts. It emphasizes clear success criteria, local-hardware-friendly execution, and validation against the user's requested outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger policy may activate the skill for broad search, bug-fix, or workflow requests where ordinary assistant behavior or a more specific skill would be a better fit.

Mitigation: Review the trigger policy before installation and narrow implicit invocation keywords if deployment requires precise routing.

Risk: The skill provides workflow and implementation guidance that can influence code, configuration, or safety decisions.

Mitigation: Review generated plans, code, commands, and configuration changes before use, and validate them against the stated success criteria.

## Reference(s):

- [Requirement Plan](artifact/references/requirement-plan.md)
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-multi-search-workflow-helper)
- [Popular ClawHub skill demand: Multi Search Engine](https://clawhub.ai/skills/multi-search-engine)
- [Ask HN: Why did my search engine post get removed?](https://news.ycombinator.com/item?id=49632482)
- [SegmentFault JavaScript topic](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript topic](https://segmentfault.com/t/typescript)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, constraints, validation checks, and remaining risks when relevant.]

## Skill Version(s):

0.20260911.40430 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
