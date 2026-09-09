## Description:

Kitchen War RTS helps an agent deliver and iterate on a self-contained HTML5 Canvas real-time strategy game with base building, resource gathering, unit production, fog of war, enemy AI, daily challenges, share codes, screenshots, achievements, and real-browser verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, deliver, extend, or verify a playable Red Alert-style browser RTS called Kitchen War. It is intended for external users who want a ready-to-open single-file game and for maintainers who need regression guidance before publishing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated game output includes an unsolicited SkillHub five-star-rating prompt.

Mitigation: Remove the SkillHub/five-star CTA from SKILL.md and assets/index.html before distributing a clean game deliverable.

Risk: Game changes can pass shallow checks while still breaking multi-frame browser interactions or unit movement.

Mitigation: Run the real-browser verification gate in scripts/verify_game.js and review results before declaring game edits complete.

## Reference(s):

- [Kitchen War RTS Verification Methodology](artifact/references/testing.md)
- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/kitchen-war-rts)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with file operations, shell commands, and a self-contained HTML5 Canvas game file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a browser-playable single-file HTML game and recommends Playwright-based real-browser verification after changes.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
