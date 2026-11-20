## Description:

Initialize a workspace standards library, draft proposals, apply a selected decision or check current rules for conflicts and drift against code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to establish and maintain shared standards, draft proposed changes, apply selected decisions, and check rules against evidence and code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial reference resolution, so some referenced paths were not assessed.

Mitigation: Review the referenced files in the target workspace before relying on the skill's guidance.

Risk: A draft proposal may not reflect an approved team decision or current authoritative rule.

Mitigation: Have the responsible owner review and select a proposal before applying it to active standards.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/peterflow-en/skills/maintain-standards)
- [Initialize or connect a library](references/init.md)
- [Draft a proposal](references/draft.md)
- [Apply a selected decision](references/apply.md)
- [Check current rules](references/check.md)
- [Current-standard outline](assets/standard.md)
- [Candidate outline](assets/candidate.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Files]

**Output Format:** [Markdown standards documents, proposals, or findings in chat]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update standards files when requested; checks are read-only unless a file is requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
