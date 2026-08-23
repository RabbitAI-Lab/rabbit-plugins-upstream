## Description:

JYS AI Shop Drama is a multi-stage workflow for creating Chinese product-placement short-drama scripts, from trope selection and plot adaptation through product selection, segment writing, and final shooting-template preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bettercalllu](https://clawhub.ai/user/bettercalllu)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill suite to plan, customize, write, and finalize product-placement short-drama scripts with reusable trope and product libraries. It is intended for agent-assisted drafting and workflow state management rather than autonomous publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated scripts can contain persuasive unsafe health, emergency, driving-related, consumer-safety, or vulnerable-audience product claims.

Mitigation: Review every generated script for advertising, medical, consumer-safety, and vulnerable-audience compliance before use.

Risk: Reusable shopping-drama patterns can steer output toward aggressive sales copy.

Mitigation: Require human editorial review before publication and keep product claims limited to verified product facts.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/bettercalllu/skills/jys-ai-shop-drama)
- [JYS workflow entrypoint](artifact/SKILL.md)
- [Workspace contract](artifact/jys/references/workspace-contract.md)
- [Creation rules](artifact/jys/references/creation-rules.md)
- [Database write guide](artifact/jys/references/db-write-guide.md)
- [S4 segment writing guide](artifact/jys-s4/references/02-逐段写作.md)
- [S5 text output guide](artifact/jys-s5/references/text-output-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured plain text generated in the agent conversation, with workflow status files used for continuation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged script-planning outputs, product facts, customized plot skeletons, complete dialogue segments, titles, character and scene notes, and final shooting-template text.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
