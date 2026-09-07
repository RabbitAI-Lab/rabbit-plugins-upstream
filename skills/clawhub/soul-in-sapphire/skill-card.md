## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give an agent Notion-backed continuity across emotional memory, state snapshots, subjective journals, and identity-change checks. It supports recall, write, setup, and audit workflows for five Notion databases plus local ambient recall artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist emotional memory, journals, self-state snapshots, and recall candidates in Notion and local workspace files.

Mitigation: Install it only when that persistence is intended, avoid writing secrets or highly private third-party details, and review journal payloads before durable writes.

Risk: The Notion integration may expose broad helper capabilities beyond a single narrow write path.

Mitigation: Use a dedicated Notion integration shared only with the intended mem, events, emotions, state, and journal databases.

Risk: Ambient recall can stage background context into the local workspace.

Mitigation: Set SIS_AMBIENT_RECALL=0 when background staging is not wanted, and record consumption only after actual use with an explicit candidate ID and turn reference.

Risk: Installing with an unpinned latest release can change behavior without an explicit version review.

Mitigation: Avoid the @latest install form when possible and review the selected release version before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Bounded emotion-linked experience recall](references/experience-recall.md)
- [Soul memory boundaries and recall observation](references/memory-transition.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; scripts emit JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or read Notion memory, event, emotion, state, journal, ambient recall, and local receipt artifacts when invoked with the required credentials and IDs.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
