## Description:

Plan a specific museum or exhibition visit with verified logistics and 90/180-minute routes, get concise on-site exhibit explanations, or turn a completed visit into a sourced memory note.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users use this skill to plan a named museum or exhibition visit, get concise on-site guidance about exhibits, or convert their own visit notes into a sourced memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Current hours, ticket rules, accessibility details, closures, and exhibition status may be wrong if they are taken from stale or unofficial sources.

Mitigation: Verify current visitor information from the venue, organizer, official ticketing, or official collection pages; include the access date and mark conflicts or gaps as unverified.

Risk: A user may ask the agent to take external actions such as buying tickets, signing in, submitting forms, or saving files.

Mitigation: Keep the default behavior to public research and in-conversation answers; do not buy tickets, log in, submit forms, or write files unless the user explicitly requests an allowed saved deliverable.

Risk: Uncertain artwork or object identification can lead to misleading on-site interpretation.

Mitigation: Ask for label text, room, title, artist, accession number, or another reliable identifier when needed, and clearly separate verified facts, interpretation, visitor reflection, and uncertainty.

## Reference(s):

- [Venue Starter Packs](references/venue-starter-packs.md)
- [Palace Museum](https://www.dpm.org.cn/)
- [National Museum of China](https://www.chnmuseum.cn/)
- [Shanghai Museum](https://www.shanghaimuseum.net/)
- [Nanjing Museum](https://www.njmuseum.com/)
- [Shaanxi History Museum](https://www.sxhm.com/)
- [Suzhou Museum](https://www.szmuseum.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown in the user's current language with source URLs, access dates, and verification-status labels where current facts are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visit brief route tables, concise exhibit explanations, or visit memory notes.]

## Skill Version(s):

2.0.1 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
