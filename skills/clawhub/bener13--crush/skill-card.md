## Description:

Builds a local relationship-analysis and conversation-practice skill from chat logs, photos, social posts, and user descriptions, with Bayesian tagging and persona generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bener13](https://clawhub.ai/user/bener13)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to parse authorized relationship materials, generate local profile artifacts, review communication patterns, and practice conversations with a simulated persona. It is intended for personal reflection and conversation rehearsal, not for harassment, stalking, deception, or non-consensual profiling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes intimate third-party data and may encourage profiling people who have not consented.

Mitigation: Use only data the user is authorized to process, avoid modeling people without consent, and keep the workflow limited to personal reflection.

Risk: Photo analysis can expose EXIF and GPS location patterns.

Mitigation: Strip EXIF and GPS metadata before analysis unless location data is explicitly authorized and necessary.

Risk: Screenshot parsing can upload images to a third-party Vision API when Vision mode is used.

Mitigation: Prefer offline OCR for sensitive screenshots, or confirm that the user understands and accepts third-party upload before using Vision mode.

Risk: Generated profile files and parsed materials may persist as plaintext under ./crushes/{slug}/.

Mitigation: Store outputs in a trusted workspace, remove plaintext files when no longer needed, and avoid sharing generated profiles.

Risk: A generated persona can be used for impersonation or deceptive contact.

Mitigation: Use simulations only for private rehearsal and do not present generated messages as if they came from the real person.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bener13/skills/crush)
- [ClawHub publisher profile](https://clawhub.ai/user/bener13)
- [OpenClaw](https://openclaw.ai)
- [Python](https://python.org)
- [Claude Code](https://claude.ai/code)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, generated skill files, parsed text outputs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes generated profile artifacts under ./crushes/{slug}/ and may invoke local Python parsers.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
