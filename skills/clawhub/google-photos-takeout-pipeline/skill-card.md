## Description:

Fully automated Google Takeout bulk download via CLI (aria2c/curl): cookie harvesting from a running browser via CDP, URL pattern construction, per-part verification, auto-unpacking, throttling and resume, plus the official server-side Google Photos to iCloud transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drpeterkalmar](https://clawhub.ai/user/drpeterkalmar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technically advanced users use this skill to automate large Google Photos Takeout downloads, verify and unpack archive parts, resume interrupted transfers, and choose the documented Google Photos to iCloud transfer path when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads live Google session cookies from a logged-in browser and writes them to disk.

Mitigation: Run only on a trusted single-user machine, keep the browser debugging port local, store the cookie jar outside shared or backed-up paths, and delete the jar and saved Takeout URL immediately after use.

Risk: The workflow uses browser debugging and local command authority during a sensitive account session.

Mitigation: Review the skill and scripts before deployment, keep the browser session under direct user control, and stop if account recovery or fraud-detection prompts appear.

Risk: A user-provided Linux browser command could introduce unintended local command execution.

Mitigation: Do not populate browser launch command parameters from untrusted input; use a reviewed local browser command only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drpeterkalmar/skills/google-photos-takeout-pipeline)
- [Pitfalls and Operational Playbook](references/pitfalls.md)
- [867 GB migration example](examples/basic-867gb-migration.md)
- [Pulling Google Takeout straight to a NAS](https://blog.omgmog.net/post/downloading-google-takeout-to-a-nas/)
- [smashah Takeout downloader gist](https://gist.github.com/smashah/67863f6c5f500c9098ad7c7e74eefc11)
- [gtr-proxy](https://github.com/nelsonjchen/gtr-proxy)
- [GooglePhotosTakeoutHelper](https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper)
- [google-photos-takeout-organizer](https://github.com/raultov/google-photos-takeout-organizer)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and Python script references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for a local CLI workflow; no autonomous login flow is described.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
