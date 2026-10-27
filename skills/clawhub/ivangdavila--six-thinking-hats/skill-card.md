## Description:

Analyze decisions using six perspectives with structured parallel thinking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users and agents use this skill to analyze decisions, problems, and ideas through De Bono's Six Thinking Hats method. It structures an analysis across facts, intuition, risks, benefits, alternatives, and process control before producing a recommendation and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local memory may retain decision-analysis preferences or recent analyses that include sensitive context.

Mitigation: Review or delete ~/six-thinking-hats/ when retained history is not desired, and avoid storing sensitive decision details unless needed.

Risk: Structured decision guidance can still be incomplete or based on uncertain facts.

Mitigation: Review the analysis, verify important facts and assumptions, and treat recommendations as decision support rather than automatic conclusions.

## Reference(s):

- [Six Thinking Hats ClawHub page](https://clawhub.ai/ivangdavila/skills/six-thinking-hats)
- [Six Thinking Hats homepage](https://clawic.com/skills/six-thinking-hats)
- [Hat details](artifact/hats.md)
- [Memory template](artifact/memory-template.md)
- [Setup guide](artifact/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown decision analysis with headings, lists, and option comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory notes in ~/six-thinking-hats/ when the user permits or preferences are learned.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
