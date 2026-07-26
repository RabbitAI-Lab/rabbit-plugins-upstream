## Description: <br>
Find contact details for accommodation listings (Airbnb, Booking.com, VRBO, Expedia). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and travel planners use this skill to run a local CLI against accommodation listing URLs and receive a contact dossier for direct booking outreach. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a local travel-concierge executable to scrape and compile contact dossiers. <br>
Mitigation: Review the executable before installing, keep it on a trusted PATH, and run it only for specific accommodation listings the user intended to investigate. <br>
Risk: Contact lookup can involve travel-site scraping and optional Google Places API use. <br>
Mitigation: Use restricted API keys, respect travel-site terms, and avoid collecting or sharing contact details beyond the user's stated booking purpose. <br>
Risk: The skill can activate on broad contact requests. <br>
Mitigation: Confirm that the user is asking about an accommodation listing before running the contact lookup workflow. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks; optional JSON from the CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes contact methods, sources, and confidence levels when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
