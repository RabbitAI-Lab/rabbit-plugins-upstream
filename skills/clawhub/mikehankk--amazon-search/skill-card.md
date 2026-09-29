## Description:

Search Amazon product listings for a keyword and return structured JSON results. Results are cached by ASIN/uuid for incremental searches and saved automatically to `results/`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikehankk](https://clawhub.ai/user/mikehankk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to search Amazon product listings by keyword, page count, product limit, and optional proxy settings, then receive structured product metadata for downstream analysis or workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe browser automation and relaxed Chromium security settings can expose the execution environment during Amazon browsing.

Mitigation: Run only in an isolated, unprivileged environment and prefer a version that keeps Chromium sandbox and security defaults enabled.

Risk: Cookie and session data can be printed or persisted locally.

Mitigation: Avoid using the skill while logged into Amazon and clear `cache/sessions`, `resultscache`, `results`, and image caches after use.

Risk: Shell execution and untrusted keyword or proxy values can increase command and network abuse exposure.

Mitigation: Do not pass untrusted keywords or proxy values, and prefer a version that uses non-shell process spawning.

## Reference(s):

- [ClawHub Amazon Search Skill](https://clawhub.ai/mikehankk/skills/amazon-search)
- [Bun Runtime](https://bun.sh)
- [Amazon](https://www.amazon.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration]

**Output Format:** [JSON result objects, saved .json files, console status text, and shell commands for setup and configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Caches ASIN/UUID values for incremental searches and can optionally download product images.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
