## Description:

Discovers inbound links to a domain, subdomain, or GitHub repo and classifies each link as controlled by the user, organic, or ambiguous.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and growth engineers use this skill to audit inbound links, separate self-created links from external references, and refresh backlink counts for reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional backlinks.sh credential can fall back to a plaintext file if OS keychain storage is unavailable.

Mitigation: Prefer BACKLINKS_SH_API_KEY for one-off runs or OS keychain storage for persistence; remove the fallback file with --logout if the same-user read risk is unacceptable.

Risk: On macOS, storing the backlinks.sh key with --login can briefly expose the secret as a process argument.

Mitigation: Avoid --login on macOS when brief local process-argument exposure is unacceptable; use the environment variable path instead.

Risk: The historical backlink writer ships with the author's example dataset and can write it to a control-panel store when --yes is used.

Mitigation: Replace the bundled SERIES data with the user's own derived history before running scripts/build-history.mjs --yes.

## Reference(s):

- [Backlink Sources Guide](references/sources.md)
- [ClawHub Skill Page](https://clawhub.ai/globalcaos/skills/backlink-audit)
- [TinkerClaw Project Homepage](https://github.com/globalcaos/tinkerclaw)
- [backlinks.sh](https://backlinks.sh)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Terminal text, Markdown guidance, and optional JSON reports or state-file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local CSV or URL-list inputs; network and write behavior depend on the selected source and explicit flags.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
