## Description:

Environment diagnostic for the PPT family that validates sn-image-base, API keys, Node runtime, and optional dependencies; it can interactively write required variables to .env and runs before sn-ppt-entry without modifying sn-image-* skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill before running the SenseNova PPT skills to confirm API keys, sn-image-base discovery, Node.js, writable deck output paths, and optional parsing/export dependencies. It reports hard failures and warnings, and can prompt for missing required environment variables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API-key environment variables and can write them to a plaintext .env file.

Mitigation: Prefer setting API keys through the normal secret manager or process environment, and use non-interactive mode when plaintext .env writes are not acceptable.

Risk: The skill checks and executes locally discovered sn-image-base tooling.

Mitigation: Install only when the local sn-image-base runner and the workspace are trusted, and avoid using an SN_IMAGE_BASE value that was not intentionally set.

Risk: The security verdict is suspicious because local environment checks combine secret handling with discovered local tooling.

Mitigation: Review the skill and scan results before deployment, and run it only in trusted directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-doctor)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text diagnostic report with optional .env file update]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports one line per check, summarizes hard-check status, and may write missing required API-key settings when run interactively.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
