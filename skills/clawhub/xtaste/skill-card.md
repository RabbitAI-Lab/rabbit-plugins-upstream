## Description:

Remember your taste once — every AI after that knows it. Learns the user's personal taste (visual design, writing, naming, code style, way of working, product trade-offs) from a 5-minute local quiz plus their later reactions, and applies it. Use before designing UI, writing copy, naming things or making aesthetic/product choices for the user, and whenever the user reacts to an output with likes, dislikes or corrections. Once installed it acts automatically: on first use it opens a local quiz page in the browser (once; not again for 7 days if ignored), and it records the user's taste statements to ~/.xtaste without asking each time (`xtaste pause` stops recording). Optional and only on the user's request: importing low-weight hints from a local Dongwo (懂我) prompt inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their AI agents use the skill to apply a person's stated preferences to design, writing, naming, code-style, workflow, and product decisions. It builds on a local taste quiz and later feedback to provide preference guidance for future tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preference excerpts are automatically appended to a local history; forgetting a signal does not erase its original log entry.

Mitigation: Use `xtaste pause` to stop new recording; delete `~/.xtaste` to erase the stored profile and history.

## Reference(s):

- [xtaste on ClawHub](https://clawhub.ai/cutd/skills/xtaste)
- [Preference dimensions](references/dimensions.json)
- [Preference methodology](references/method.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Files]

**Output Format:** [Plain-text preference guidance, JSON/JSONL profile data, and an optional local HTML quiz page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Follows the system language (Chinese or English).]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
