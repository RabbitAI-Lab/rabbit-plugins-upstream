## Description:

Inspect and export objects from CorelDRAW CDR files via COM automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to inspect CorelDRAW CDR documents and export selected pages, layers, shapes, or object ranges into shareable asset files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspection metadata and manifests may include local file paths, private usernames, document object names, or project-specific notes.

Mitigation: Review generated metadata before sharing and remove local paths or sensitive document details.

Risk: The skill automates local CorelDRAW and opens user-selected CDR files on the host system.

Mitigation: Install and run it only where local CorelDRAW automation is expected, and use CDR files and output folders chosen by the user.

Risk: Exports may differ from the source document when complex effects, lenses, transparencies, or fonts are rendered by CorelDRAW.

Mitigation: Validate exported file counts, byte sizes, transparency, and visual previews before relying on or publishing generated assets.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell command examples; generated artifacts may include JSON metadata, CSV manifests, previews, and exported image or vector files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against local CorelDRAW through COM automation and depends on the user's selected CDR files and output folders.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
