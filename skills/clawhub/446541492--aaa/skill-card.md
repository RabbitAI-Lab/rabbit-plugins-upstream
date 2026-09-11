## Description:

AI搜问 helps authorized agents search DingTalk people, enterprise content, and behavior records, then route follow-up detail lookup or actions to the appropriate DingTalk skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[446541492](https://clawhub.ai/user/446541492)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents with authorized DingTalk access use this skill to locate colleagues by name, job number, department, responsibility, supervisor or subordinate relationship, or phone clue. They also use it to find enterprise documents, messages, mail, meeting notes, and behavior records before handing off reading, writing, or communication actions to the relevant DingTalk skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill searches sensitive DingTalk people, messages, mail, documents, and activity records.

Mitigation: Install only where DingTalk permissions and user authorization are already governed; ask for narrower scope before broad behavior searches and avoid non-work-related employee lookup or communication profiling.

Risk: Command examples pass user text into CLI arguments.

Mitigation: Run CLI calls with structured argv-style execution or strict escaping, and preserve user query text as a single argument.

Risk: Ambiguous person search results could cause the agent to act on the wrong employee.

Mitigation: Show multiple candidates for user selection and use contact detail lookup for disambiguation instead of defaulting to the first result.

## Reference(s):

- [aisearch command reference](references/aisearch.md)
- [aisearch intent guide](references/intent-guide.md)
- [aisearch lite recipes](references/lite-recipes.md)
- [ClawHub skill page](https://clawhub.ai/446541492/skills/aaa)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON parsing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require the dws binary and should include --format json when using dws aisearch.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
