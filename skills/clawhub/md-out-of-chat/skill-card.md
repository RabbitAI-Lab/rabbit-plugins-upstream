## Description:

Converts a named Markdown file into a mobile-friendly local HTML page for reading and sharing from phone browsers, with public URL output only after explicit user request and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI-agent users, and documentation authors use this skill to convert a specific Markdown report, note, or chat export into a local HTML page that remains readable on mobile devices. It is intended for local-first sharing workflows where public publishing requires separate explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the named Markdown file and may embed local images referenced from the same folder or its subfolders.

Mitigation: Run it only on files intended for conversion and review the logged embedded image paths when local images are present.

Risk: Published HTML could expose private Markdown content if the user opts into public deployment.

Mitigation: Keep local HTML as the default and review the generated page before confirming any public publishing step.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/md-out-of-chat)
- [Live HTML demo](https://2uf0a7axwwwr.space.minimaxi.com)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated artifact is a local HTML file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first output; public URL only after explicit user request and confirmation; no screenshot or image output.]

## Skill Version(s):

1.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
