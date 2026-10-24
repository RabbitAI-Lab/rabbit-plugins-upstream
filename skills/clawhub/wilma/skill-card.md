## Description:

Access Finland's Wilma school system from AI agents to fetch schedules, homework, exams, grades, lesson notes, absences, messages, news, printouts, and linked resources through WilmAI MCP tools or the wilma CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and guardians use this skill to retrieve and summarize school updates from Finland's Wilma system, including schedules, homework, grades, messages, absences, and related documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: School information read by the assistant is sent to its AI provider.

Mitigation: Connect only accounts you are authorized to access, and narrow requests to a specific child when appropriate.

Risk: Saved Wilma credentials and optional MFA secrets remain on the computer or in agent secret settings.

Mitigation: Protect the computer and secret settings; use account removal or clear the Wilma configuration to remove saved credentials, since logout retains them.

Risk: Installation and updates execute externally distributed npm code.

Mitigation: Review and approve the package installation and updates in the environment where the skill runs.

## Reference(s):

- [Wilma skill release](https://clawhub.ai/aikarjal/skills/wilma)
- [WilmAI project repository](https://github.com/aikarjal/wilmai)
- [WilmAI website](https://wilm.ai)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Natural-language summaries and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries prioritize actionable school updates; CLI and MCP results are structured per child.]

## Skill Version(s):

2.2.0 (source: skill frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
