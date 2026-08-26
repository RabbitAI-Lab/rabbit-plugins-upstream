## Description:

PractiTest lets agents read, create, update, and delete PractiTest project and test records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and QA teams use this skill to operate PractiTest projects and tests from an agent after connecting their PractiTest account through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OOMOL brokers access to the user's PractiTest account.

Mitigation: Install the skill only when the user trusts OOMOL to manage that account connection.

Risk: Create and update actions can change PractiTest records.

Mitigation: Review the exact payload and expected effect before approving state-changing actions.

Risk: The delete_test action is described as permanent.

Mitigation: Confirm the target test and require explicit user approval before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-practitest)
- [PractiTest homepage](https://www.practitest.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live PractiTest connector schemas before actions; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
