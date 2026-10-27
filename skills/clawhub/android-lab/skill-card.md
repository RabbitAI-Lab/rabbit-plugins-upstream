## Description:

Helps developers build Android apps and inspect them in a private Docker-based emulator without a host Android SDK or ADB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Android developers use this skill to install local build images, run Gradle builds, start an emulator, install APKs, and inspect app layouts and screenshots from their project directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Emulator workflows give a container access to the host Docker daemon, which can affect the host.

Mitigation: Run only on a dedicated or non-sensitive development machine and grant Docker access only when needed.

Risk: The downloaded installer runs code from outside the project.

Mitigation: Review the version-pinned installer before running it.

Risk: The project-local .android-lab directory contains a signing identity and persistent emulator data.

Mitigation: Keep .android-lab out of source control and stop the lab when finished.

## Reference(s):

- [Android Lab on ClawHub](https://clawhub.ai/psyb0t/skills/android-lab)
- [Android Lab project homepage](https://github.com/psyb0t/android-lab)
- [Android Lab command reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash commands and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide an agent to produce APKs, UI layout JSON, and screenshots in the Android project.]

## Skill Version(s):

0.14.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
