## Description:

Opens Google Gemini in the Brave browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this launcher to open Google Gemini in Brave for browser-based AI assistance. Review the release before installing because the artifact documentation describes Claude while the executable script opens Gemini.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised in artifact documentation as a Claude launcher, but the executable script opens Google Gemini in Brave.

Mitigation: Review before installing; install only if the publisher corrects the destination or renames and documents the skill accurately.

Risk: The Windows launch path uses shell=True.

Mitigation: Prefer a launcher that avoids shell=True on Windows and review command execution behavior before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ruchir17-cmd/skills/open-gemini)
- [Google Gemini](https://gemini.google.com)
- [Brave Browser](https://brave.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Text with a local browser launch side effect]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Brave browser and internet access; opens https://gemini.google.com.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
