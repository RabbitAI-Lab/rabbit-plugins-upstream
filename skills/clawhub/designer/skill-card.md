## Description: <br>
Operates as the designer on a job: decides what to make, makes it, defends it in review, and hands over files that can actually be built. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to act as a practical designer for product, brand, client, interface, accessibility, handoff, marketing, mobile, or print work. It produces design artifacts, design-system guidance, critiques, specifications, and review findings rather than frontend implementation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps persistent local memory about brands, projects, stakeholders, licences, reviews, and design decisions. <br>
Mitigation: Install it only when that ongoing memory is desired, and periodically review the Clawic data folders for stale or unwanted notes. <br>
Risk: The skill has broad local data access across the declared Clawic design, contact, project, finance, profile, and legacy design folders. <br>
Mitigation: Keep credentials out of those folders, store only pointers such as environment variable or keychain references, and review automatic note writes during sensitive client work. <br>
Risk: Design proposals, critiques, or specifications may be incomplete or unsuitable for a particular brand, accessibility target, platform, printer, or engineering constraint. <br>
Mitigation: Review outputs against the stated constraints, accessibility requirements, platform rules, and handoff checklist before using them with clients or implementers. <br>


## Reference(s): <br>
- [Designer on ClawHub](https://clawhub.ai/ivangdavila/skills/designer) <br>
- [Designer homepage](https://clawic.com/skills/designer) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Accessibility guidance](artifact/accessibility.md) <br>
- [Handoff guidance](artifact/handoff.md) <br>
- [Memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown prose with structured specifications, tables, checklists, token names, code or configuration snippets when useful, and local note updates when durable design memory is produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local Clawic data folders declared in the skill metadata; does not call external services by itself.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
