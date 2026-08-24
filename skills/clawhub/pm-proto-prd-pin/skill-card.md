## Description:

A plug-and-play skill that helps agents add an interactive PRD pinning, annotation, multi-version specification, and export workflow to existing HTML prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, designers, and UI engineers use this skill to turn static HTML prototypes into reviewable PRD workspaces with pinned requirements, versioned specification data, Markdown and Mermaid authoring, and exportable PRD documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-synced PRD data may be public-readable or externally hosted.

Mitigation: Use the cloud mode only for data approved for external hosting, or use the local Node.js mode for confidential prototypes.

Risk: Write credentials for JSONBin or GitHub can be entered into and retained by the browser workflow.

Mitigation: Use narrowly scoped throwaway tokens where possible, rotate tokens after use, and avoid entering long-lived credentials into shared browsers.

Risk: The local service writes PRD data files to the prototype project and should not be exposed broadly.

Mitigation: Run the local server only on a trusted machine and network, and stop it when editing is complete.

Risk: The injector modifies HTML files and can replace bundled vendor assets.

Mitigation: Back up or version-control the target prototype before injection and review the resulting file changes before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)
- [JSONBin cloud storage service](https://jsonbin.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, configuration steps, and generated or modified prototype files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HTML script injections, JavaScript data files, local server startup commands, and PRD exports.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
