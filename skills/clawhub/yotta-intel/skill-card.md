## Description:

Yuanqing yotta-intel extracts and normalizes threat-intelligence IOCs from local text, logs, reports, and phishing emails, handles defanged forms, and exports text, JSON, CSV, or STIX-lite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security analysts, incident responders, and developers use this skill to extract, deduplicate, normalize, defang, refang, and convert candidate IOCs from already-collected threat reports, phishing emails, logs, or other authorized text sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can write into multiple agent skill folders and overwrite an existing yotta-intel skill directory without confirmation.

Mitigation: Review the installer before running it, prefer a pinned version with an explicit --agent or --dir target, avoid global installation unless intended, and back up or remove an existing skill directory first.

Risk: The parser outputs candidate indicators rather than maliciousness determinations.

Mitigation: Treat extracted IOCs as analysis candidates and verify them with authorized human review or separate intelligence sources before operational action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-intel)
- [IOC Type and Normalization Rules](references/ioc-spec.md)
- [Defang and Refang Rules](references/defang-rules.md)
- [STIX-lite Output Specification](references/stix-lite-spec.md)
- [npm package @yottameta/yotta-intel](https://www.npmjs.com/package/@yottameta/yotta-intel)

## Skill Output:

**Output Type(s):** [text, JSON, CSV, STIX-lite, shell commands, guidance]

**Output Format:** [Text reports, JSON objects, CSV rows, or STIX 2.1 Bundle JSON, often accompanied by shell commands for the local parser.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes local input only and reports candidate indicators with normalized and defanged values.]

## Skill Version(s):

0.1.2 (source: release metadata; artifact files report 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
