## Description:

Lan Knowledge Share helps an agent publish a local folder as an unauthenticated LAN web knowledge base for browsing and searching Markdown, spreadsheets, HTML reports, images, and media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vesentanger](https://clawhub.ai/user/vesentanger)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, teams, and developers use this skill to share a tightly scoped local folder with colleagues on the same LAN as a browser-accessible knowledge base. It is useful for temporary internal document review, local file browsing, and offline LAN sharing where authentication is not required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unauthenticated LAN server can expose every browsable file in the selected folder to anyone who can reach the network.

Mitigation: Use only a tightly scoped folder that contains files intended for sharing, and do not share home directories, repositories, secrets, internal reports, or personal data.

Risk: A LAN link may be treated as private even though it is accessible to other reachable devices on the network.

Mitigation: Treat the LAN URL as public within the network, avoid forwarding it to public or untrusted networks, and limit firewall access to trusted private networks.

Risk: Exclude lists, hidden directories, and folder naming conventions are not an access-control system.

Mitigation: Remove sensitive files from the shared tree before launch instead of relying on exclusions or hidden paths to protect them.

Risk: Shared HTML reports or documents may contain active or untrusted content that will be rendered in users' browsers.

Mitigation: Share only trusted documents and reports, and review folder contents before starting the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vesentanger/skills/lan-folder-share)
- [README](README.md)
- [SkillHub listing material](references/skillhub-listing.md)
- [Bundled third-party library inventory](assets/runtime/assets/vendor/THIRD-PARTY.md)
- [docsify](https://github.com/docsifyjs/docsify)
- [marked](https://github.com/markedjs/marked)
- [SheetJS](https://github.com/SheetJS/sheetjs)
- [mammoth.js](https://github.com/mwilliamson/mammoth.js)
- [Prism](https://github.com/PrismJS/prism)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and operational warnings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides the agent through confirming folder scope and authentication risk before launching a local Node.js HTTP server.]

## Skill Version(s):

1.0.12 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
