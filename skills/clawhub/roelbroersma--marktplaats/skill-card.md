## Description: <br>
Helps agents prepare, place, verify, and locally track Marktplaats advertisements with copy-quality, preflight, live-verification, and register-update checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[roelbroersma](https://clawhub.ai/user/roelbroersma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to prepare normal Marktplaats sale listings, choose categories, quality-check listing copy, guide browser-based posting after explicit approval, verify the live listing, and update local ad records. <br>

### Deployment Geography for Use: <br>
Netherlands <br>

## Known Risks and Mitigations: <br>
Risk: Browser probes can inspect pages in the user's logged-in Safari session and may accept user-supplied URLs without an enforced Marktplaats-only scope. <br>
Mitigation: Keep Safari on the intended Marktplaats page before probing, avoid arbitrary --url or --open-background targets, and use the browser checks only for the current listing flow. <br>
Risk: Saved ad records and snapshots may contain private listing details or form-derived data. <br>
Mitigation: Treat local ad records and snapshots as private, store them in user-controlled locations, and review them before sharing or committing. <br>
Risk: A listing could be published, reposted, or promoted with unintended content or paid options if approval gates are bypassed. <br>
Mitigation: Require explicit approval for each advertisement, keep paid features disabled by default, and complete copy-QA, preflight, live verification, and register update checks in order. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/roelbroersma/skills/marktplaats) <br>
- [Marktplaats Seller Assistant - English Guide](references/guide-en.md) <br>
- [Marktplaats Verkoopassistent - Nederlandse Handleiding](references/handleiding-nl.md) <br>
- [Robust Posting Checklist](references/robust-posting-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON ad records, and local file updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a logged-in Safari session for browser-based Marktplaats checks; stores local ad records and snapshots when used.] <br>

## Skill Version(s): <br>
0.6.1 (source: server release, package.json, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
