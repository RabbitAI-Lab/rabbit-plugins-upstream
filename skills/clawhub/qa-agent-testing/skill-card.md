## Description:

Guides QA teams in designing risk-based tests for AI agents across functionality, safety, controllability, reliability, factuality, reasoning, and tool use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to plan and document AI-agent tests, including prompt-injection defenses, hallucinations, tool calls, and human oversight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms could lead to unnecessary shell commands or external fetching during testing.

Mitigation: Only permit Bash or WebFetch when needed for the user's specific testing task; review the proposed action before use.

## Reference(s):

- [Agent nine-dimension test framework](references/test-framework.md)
- [qa-agent-testing release on ClawHub](https://clawhub.ai/kokxi/skills/qa-agent-testing)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown test plan, test-case table, and assessment checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Test cases have unique IDs and requirement links; coverage gaps and risk levels are identified.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
