## Description:

Archive public Instagram media through InstaCognito with bounded archive/sync runs, section-aware outcomes, durable receipts, and optional local ZIP export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[saju01](https://clawhub.ai/user/saju01)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use FrameFerry to run bounded local archives or repeat syncs of public Instagram profile media they are allowed to preserve. It helps agents bootstrap the Node CLI, run archive/status/export commands, and report section-level outcomes without claiming guaranteed completeness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill requires npm and Playwright setup and saves public media to local storage.

Mitigation: Install only in an environment where local Node tooling and saved media are acceptable, and use a dedicated output directory.

Risk: Archiving media without authorization can violate rights, privacy expectations, or provider terms.

Mitigation: Archive only public profiles and media that the user has rights or explicit permission to preserve.

Risk: Attaching to an existing browser debugging endpoint can expose browser-session state.

Mitigation: Avoid CDP attachment to a personal browser profile unless the user intentionally accepts that exposure risk.

Risk: Provider limits, hidden content, deleted content, CAPTCHA, or selector changes can make results partial or unavailable.

Mitigation: Use the recorded section outcomes and status files, and do not treat a successful ZIP package as proof of complete archival coverage.

## Reference(s):

- [FrameFerry ClawHub release](https://clawhub.ai/saju01/skills/frameferry)
- [FrameFerry repository](https://github.com/saju01/frameferry)
- [InstaCognito public media page](https://instacognito.com/en/photo)
- [Model-tiered orchestration guide](references/orchestration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and local archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bounded local media archives, JSON receipts, manifest/status files, and optional ZIP exports through the FrameFerry CLI.]

## Skill Version(s):

0.2.1 (source: changelog and package.json, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
