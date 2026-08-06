## Description:

Generates polished card-style HTML book excerpt articles from a book or author input and adds them to a local single-page bookshelf for later browsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

External users and content creators use this skill to turn book or author inputs into reusable reading-summary capsules. It helps maintain a local bookshelf of generated HTML excerpts for review, sharing, or later browsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically creates local HTML files and updates a persistent bookshelf registry.

Mitigation: Install and run it only when this state-changing local workflow is expected; review generated paths and bookshelf updates before relying on the output.

Risk: Generated quote and summary content may include inaccurate, misattributed, or copyright-sensitive text.

Mitigation: Review generated book excerpts for accuracy, attribution, and copyright suitability before sharing or publishing them.

Risk: Trigger phrases may invoke a workflow that writes files without an additional confirmation step.

Mitigation: Use the skill in a workspace where automatic HTML and registry updates are acceptable, and keep a separate review step for public distribution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zhouq2039-lang/skills/capsule-bookshelf-skill)
- [README](artifact/README.md)
- [Skill workflow](artifact/SKILL.md)
- [Template usage guide](artifact/template-usage.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance, Files]

**Output Format:** [HTML files, JSON data, and concise text status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local HTML outputs, capsule-registry.json, and bookshelf.html when a new capsule is generated.]

## Skill Version(s):

0.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
