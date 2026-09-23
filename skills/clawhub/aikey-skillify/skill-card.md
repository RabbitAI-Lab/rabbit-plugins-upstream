## Description:

AI KEY·做成一个技能 turns a completed and verified agent workflow from the current session into a reusable local skill, with gates for evidence, boundaries, self-checks, and handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill after a task has succeeded to distill the actual process, completion evidence, boundaries, and evaluation checks into a reusable skill directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be activated by casual wording that resembles a request to save a workflow.

Mitigation: Use explicit slash commands when possible and confirm the work is completed, verified, and likely to recur before generating a skill.

Risk: A generated skill may preserve an unverified or misleading process if the completed-work gate is skipped.

Mitigation: Review the generated skill and memory entry, require concrete completion evidence, and run at least the main scenario before relying on the result.

Risk: Premature public release can make a newly formed skill harder to correct.

Mitigation: Keep the default handoff local and require explicit human approval before publishing to public channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-skillify)
- [规则卡](references/规则卡.md)
- [AI KEY README upgrade note](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions and local skill files, with optional shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local reusable-skill artifacts that require review before relying on them or publishing them.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
