## Description:

An on-demand identity assistant that uses a person's AXIOM, ETHOS, and MODUS profiles to guide requested reasoning, writing, evaluation, and profile updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[capachow](https://clawhub.ai/user/capachow)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use LENS when they explicitly want an agent to reason, write, evaluate, or decide in alignment with their personal context, values, and voice. They can also calibrate or distill their LENS profile on demand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can enable ongoing chat collection across apps, and collected chats may be processed by the configured AI model.

Mitigation: Choose chat sources and recurring jobs deliberately; review workspace profiles before importing them, and remember that redaction cannot guarantee confidentiality.

Risk: Migration can discard existing files, while LENS profiles persist over time.

Mitigation: Back up existing .lens directories before setup and review profiles before importing them.

Risk: Host automation behavior was not exercised during the security review.

Mitigation: Review automation choices and behavior in the target host before enabling recurring collection.

## Reference(s):

- [LENS on ClawHub](https://clawhub.ai/capachow/skills/lens)
- [Publisher profile: capachow](https://clawhub.ai/user/capachow)
- [Alignment scales](artifact/references/alignment-scales.md)
- [Resolve protocol](artifact/references/resolve-protocol.md)
- [Trinity definitions](artifact/references/trinity-definitions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Natural-language responses and YAML or JSON profile configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are tailored to the user's supplied or calibrated LENS profile.]

## Skill Version(s):

2.0.0 (source: package.json; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
