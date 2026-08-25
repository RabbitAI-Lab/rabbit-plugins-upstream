## Description:

Generate a personalized, breed-and-age-aware dog training program: 5-minute daily exercise plans targeting the owner's specific behavior problems, week-by-week progression, breed drive profiles (herding/hunting/guarding energy outlets), and progress tracking with automatic plan adjustment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External dog owners and agents helping with pet questions use this skill to create breed- and age-aware, force-free training plans, progress guidance, and referral-aware support for common dog behavior concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may try to use ordinary training guidance for aggression, bites, severe anxiety, pain, sudden behavior changes, respiratory limits, heat risk, injury, puppy, or senior-dog concerns.

Mitigation: Use the red-flag screening guidance and consult a veterinarian or credentialed behavior professional for those cases.

Risk: The skill may run an included Python script and keep a local training log.

Mitigation: Review commands before execution and avoid entering sensitive personal information in session notes.

## Reference(s):

- [Dog Train-O-Matic ClawHub release](https://clawhub.ai/voronindenis5/skills/dog-train-o-matic)
- [Breed Drive Profiles](references/breed-drives.md)
- [Behavior Protocols](references/protocols.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown/plain text plans with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May keep a local JSON training log when progress logging commands are used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
