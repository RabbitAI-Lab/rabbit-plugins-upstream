## Description:

Guides creators through defining consistent AI video characters and hero props with detailed passports, turnaround and expression sheets, measured voice lines, reusable prompts, and validation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers, video creators, and developers use this skill to define a character or hero prop clearly, keep its appearance and performance consistent across AI-generated shots, and check prompts and takes before production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional shoot.ts renderer can expose local files outside its asset folder.

Mitigation: Avoid using it until requests are limited to approved assets, the server binds to loopback, permissive CORS is removed, and errors reliably trigger cleanup.

Risk: Confidential artwork or voice recordings may be sent to hosted generation services.

Mitigation: Choose approved providers before submitting confidential material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/character-passport)
- [Repository homepage listed in metadata](https://github.com/vargHQ/skills/tree/main/character-passport)
- [Character passport guide](artifact/SKILL.md)
- [Passport format and examples](artifact/references/passport.md)
- [Turnaround and expression sheets](artifact/references/sheets.md)
- [Character acting and expressions](artifact/references/acting.md)
- [Voice design and measurement](artifact/references/voice.md)
- [Code-based character routes](artifact/references/code.md)
- [Blind-judged skill evaluation](https://claude.ai/artifact/AJ1g4Qren3ZvwERSwrQigt)

## Skill Output:

**Output Type(s):** [Markdown, Text, Code, Shell commands, Guidance]

**Output Format:** [Markdown guides and cast files, reusable prompt text, shell commands, and optional code examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides preparation of character and prop passports, visual sheets, expression and voice specifications, shot prompts, and review checks. Generated images and voice takes depend on the selected tools and services.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
