## Description:

Manages medication schedules, detects drug interactions, tracks adherence, and generates refill reminders. Produces safe daily schedules and printable checklists from a medication list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and care-support workflows can use this skill to organize medication timing, review a limited built-in set of drug interaction warnings, track doses taken or missed, and prepare refill reminders and printable daily checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles health-related medication schedules and a limited built-in interaction database that may be incomplete or unsuitable for clinical decisions.

Mitigation: Treat outputs as informational organization aids and verify medication decisions with a clinician, pharmacist, or authoritative drug-interaction database.

Risk: The adherence feature creates a local health-related history file at ~/.medication_commander_adherence.json.

Mitigation: Avoid using adherence tracking on shared machines unless local account protections are appropriate, and delete the file when the retained history is no longer needed.

## Reference(s):

- [Interaction Database Reference](references/interactions.md)
- [Usage Guide](references/usage.md)
- [Server-Resolved GitHub Repository](https://github.com/voronindenis5/medication-commander)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/medication-commander)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON command output, plain-text printable checklists, Markdown documentation, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The adherence command stores local history in ~/.medication_commander_adherence.json.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
