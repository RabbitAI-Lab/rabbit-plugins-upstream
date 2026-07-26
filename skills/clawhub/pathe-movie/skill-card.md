## Description: <br>
Lookup Pathé Netherlands movies, posters, descriptions, cinemas, and showtimes via the Pathé JSON APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[humboldtjs](https://clawhub.ai/user/humboldtjs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and assistants use this skill to answer Pathé Netherlands movie questions, including title lookup, posters, ratings, descriptions, cinema availability, and showtimes. <br>

### Deployment Geography for Use: <br>
Global, limited to Pathé Netherlands movie data. <br>

## Known Risks and Mitigations: <br>
Risk: Pathé API availability or response changes could affect movie, cinema, poster, and showtime answers. <br>
Mitigation: Ground responses in returned API data and clearly report empty, missing, or incomplete results. <br>
Risk: Poster and still image delivery may temporarily save media files locally for WhatsApp delivery. <br>
Mitigation: Download media only when requested, use temporary paths, and remove temporary files when practical. <br>


## Reference(s): <br>
- [Pathé API Reference](references/api.md) <br>
- [Pathé JSON API](https://www.pathe.nl/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with JSON-derived movie details and optional local media file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include locally downloaded poster or still image files for WhatsApp delivery when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
