## Description:

A CLI skill for collecting public Xiaohongshu note engagement metrics, including likes, saves, comment counts, share counts, note titles, and note IDs, with batch submission, polling, and CSV export support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill to submit batches of public Xiaohongshu note URLs with xsec_token parameters, poll collection tasks, summarize engagement metrics, and export results as CSV files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party backend receives Xiaohongshu note URLs, xsec_token parameters, task results, and a service account token.

Mitigation: Install only if the user trusts the publisher and service; submit only public note URLs and avoid sensitive links or shared credentials.

Risk: Security evidence reports an insecure default connection for a skill that handles account tokens and submitted links.

Mitigation: Configure an HTTPS backend before login or submission and avoid sending credentials or xsec_token values over untrusted networks.

Risk: The local service token is saved under ~/.xhs-platform/config.json and may be migrated from ~/.xhs-convert/config.json.

Mitigation: Use a private machine or isolated XHS_CONFIG_PATH, do not commit configuration files, and logout or clear tokens when access is no longer needed.

Risk: TLS verification can be weakened through the insecure configuration path.

Mitigation: Do not enable insecure TLS except in controlled testing, and restore secure settings for normal use.

Risk: Collection can fail or return missing metric fields due to note visibility, rendering, service, or platform controls.

Mitigation: Report fail_reason values directly, distinguish missing metrics from zero, and avoid promising complete collection success.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cuiyunhai/skills/xhs-dpt)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, CSV files]

**Output Format:** [JSON result envelopes on stdout, progress and prompts on stderr, and optional CSV export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=18, authenticated service access, and Xiaohongshu note URLs containing xsec_token; batches are limited to 1-50 URLs.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
