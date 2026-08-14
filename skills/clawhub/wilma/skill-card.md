## Description:

Access Finland's Wilma school system from AI agents to fetch schedules, homework, exams, grades, attendance notes, messages, news, and linked news resources through the wilma CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and agents assisting them use this skill to prepare concise school briefings, check upcoming obligations, and retrieve relevant Wilma messages, news, homework, schedules, exams, grades, attendance notes, and attachments.

### Deployment Geography for Use:

Finland

## Known Risks and Mitigations:

Risk: The skill can expose sensitive student information such as grades, attendance notes, messages, and downloaded attachments.

Mitigation: Install it only for intended Wilma access, treat all retrieved outputs as sensitive, and keep downloads limited to items needed for the current task.

Risk: The CLI depends on a local Wilma session credential file created during interactive setup.

Mitigation: Use a user-managed local config file, refresh or clear it when authentication expires, and avoid placing credentials in prompts or generated artifacts.

Risk: Linked news resources may be external pages, private documents, or non-file web pages.

Mitigation: Attempt a single CLI download, honor the reported downloaded, not_a_file, or error status, and avoid repeated retries or sharing Wilma credentials with external links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aikarjal/skills/wilma)
- [Wilma CLI website](https://wilm.ai)
- [Wilma CLI GitHub repository](https://github.com/aikarjal/wilmai)
- [npm package @wilm-ai/wilma-cli](https://www.npmjs.com/package/@wilm-ai/wilma-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash examples and JSON-oriented CLI command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers non-interactive --json CLI output; linked news resources may produce task-scoped downloaded files when requested.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
